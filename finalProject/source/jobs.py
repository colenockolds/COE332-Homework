import uuid
import os
from hotqueue import HotQueue
from redis import StrictRedis

redis_ip = os.environ.get('REDIS_IP')
if not redis_ip:
    raise Exception()
rd=StrictRedis(host=redis_ip, port=6379, db=0)
rd_plot=StrictRedis(host=redis_ip, port=6379, db=2)
q = HotQueue("queue", host=redis_ip, port=6379, db=1)

def _generate_jid():
    return str(uuid.uuid4())

def _generate_job_key(jid):
    return 'job.{}'.format(jid)

def _instantiate_job(jid, restaurant, status):
    if type(jid) == str:
        return {'id': jid,
                'restaurant': restaurant,
                'status': status
        }
    return {'id': jid.decode('utf-8'),
            'restaurant': restaurant.decode('utf-8'),
            'status': status.decode('utf-8')
    }

def _save_job(job_key, job_dict):
    rd_plot.hmset(job_key, job_dict)

def _queue_job(jid):
    q.put(jid)

def add_job(restaurant, status="submitted"):
    jid = _generate_jid()
    job_dict = _instantiate_job(jid, restaurant, status)
    _save_job(_generate_job_key(jid), job_dict)
    _queue_job(jid)
    return job_dict

def update_job_status(jid, new_status):
    jid, restaurant, status = rd_plot.hmget(_generate_job_key(jid), 'id', 'restaurant', 'status') 
    job = _instantiate_job(jid, restaurant, status)
    IP = os.environ.get('WORKER_IP')

    if job:                                                                 
        job['status'] = new_status     
        if new_status == 'in progress':
            job['IP'] = IP             
        _save_job(_generate_job_key(job['id']), job)
    else:
        raise Exception()
