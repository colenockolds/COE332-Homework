import time
import os
from jobs import q

@q.worker
def execute_job(jid):
    worker_ip = os.environ.get('WORKER_IP')
    update_job_status(jid, worker_ip, 'in progress')
    time.sleep(15)
    update_job_status(jid, worker_ip, 'complete')

execute_job()
