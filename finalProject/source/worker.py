import datetime
from hotqueue import HotQueue
from jobs import rd, rd_plot, q, update_job_status
import matplotlib.pyplot as plt

@q.worker
def execute_job(jid):
    update_job_status(jid, 'in progress')
    restaurant = rd_plot.hget(f'job.{jid}', 'restaurant').decode('utf-8')
    dates = []
    scores = []
    for key in rd.keys():
        if rd.hget(key,'Restaurant Name').decode('utf-8') == restaurant:
            date = rd.hget(key,'Date of Inspection').decode('utf-8')
            score = rd.hget(key,'Inspection Score').decode('utf-8')
            dates.append(datetime.datetime.strptime(date, "%m/%d/%Y"))
            scores.append(int(score))
    x = dates
    y = scores
    plt.figure(figsize=(10, 10))
    plt.plot_date(x,y)
    restaurant = restaurant.replace(' ','-')
    plt.savefig(str(restaurant)+'.png')
    file_bytes = open(str(restaurant)+'.png', 'rb').read()
    rd_plot.set(str(restaurant)+'_plot', file_bytes)
    print('Plot Key: '+str(restaurant)+'_plot'+"\n")
    update_job_status(jid, 'complete')

execute_job()
