import time
from hotqueue import HotQueue
from jobs import q, update_job_status, plot

@q.worker
def execute_job(jid):
    update_job_status(jid, 'in progress')
    plot(jid)
    update_job_status(jid, 'complete')

execute_job()
