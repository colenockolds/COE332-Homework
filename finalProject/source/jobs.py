import uuid
import os
from hotqueue import HotQueue
from redis import StrictRedis
import matplotlib.pyplot as plt

redis_ip = os.environ.get('REDIS_IP')
if not redis_ip:
    raise Exception()
rd=StrictRedis(host=redis_ip, port=6379, db=0)
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
            'restaurant': jid.decode('utf-8'),
            'status': status.decode('utf-8')
    }

def _save_job(job_key, job_dict):
    rd.hmset(job_key, job_dict)

def _queue_job(jid):
    q.put(jid)

def add_job(restaurant, status="submitted"):
    jid = _generate_jid()
    job_dict = _instantiate_job(jid, restaurant, status)
    _save_job(_generate_job_key(jid), job_dict)
    _queue_job(jid)
    return job_dict

def update_job_status(jid, new_status):
    jid, restaurant, status = rd.hmget(_generate_job_key(jid), 'id', 'restaurant', 'status') 
    job = _instantiate_job(jid, restaurant, status)
    IP = os.environ.get('WORKER_IP')

    if job:                                                                 
        job['status'] = new_status     
        if new_status == 'in progress':
            job['IP'] = IP             
        _save_job(_generate_job_key(job['id']), job)
    else:
        raise Exception()
    return "Job Key: "+str(_generate_job_key(job['id']))+"\n"

def plot(jid):
    restaurant = hget(jid, 'restaurant')
    restaurant = restaurant.replace('%',' ')
    #restaurant = restaurant.replace('[', '')
    #restaurant = restaurant.replace("'", '')
    #restaurant = restaurant.replace(']', '')
    dates = []
    score = []
    for key in rd.keys():
        if rd.hget(key,'Restaurant Name') == restaurant:
            date = rd.hget(key,'Inspection Date')
            date = date.replace('[', '')
            date = date.replace("'", '')
            date = date.replace(']', '')
            score = rd.hget(key,'Score')
            score = score.replace('[', '')
            score = score.replace("'", '')
            score = score.replace(']', '')
            dates = dates+datetime.datetime.strptime(date, "%m-%d-%Y")
            return dates
            scores = scores+int(score)
            return scores
    x = dates
    y = scores
    plt.plot(x,y)
    restaurant = restaurant.replace('%','-')
    plt.savefig(str(restaurant)+'.png')
    file_bytes = open(str(restaurant)+'.png', 'rb').read()
    rd.set(str(restaurant)+'_plot', file_bytes)
    return 'Plot Key: '+str(restaurant)+'_plot'+"\n"
