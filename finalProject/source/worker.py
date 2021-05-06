import time
from hotqueue import HotQueue
from jobs import rd, q, update_job_status, plot

@q.worker
def execute_job(jid):
    update_job_status(jid, 'in progress')
    #plot(jid)
    restaurant = rd.hget(jid, 'restaurant')
    restaurant = str(restaurant)
    restaurant = restaurant.replace('%',' ')
    #restaurant = restaurant.replace('[', '')
    #restaurant = restaurant.replace("'", '')
    #restaurant = restaurant.replace(']', '')
    dates = []
    scores = []
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
            scores = scores+int(score)
    x = dates
    y = scores
    plt.plot(x,y)
    restaurant = restaurant.replace('%','-')
    plt.savefig(str(restaurant)+'.png')
    file_bytes = open(str(restaurant)+'.png', 'rb').read()
    rd.set(str(restaurant)+'_plot', file_bytes)
    print('Plot Key: '+str(restaurant)+'_plot'+"\n")
    update_job_status(jid, 'complete')

execute_job()
