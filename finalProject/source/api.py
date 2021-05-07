import json
import redis
from flask import Flask, request, send_file
import os
import jobs
import datetime

app = Flask(__name__)

redis_ip = os.environ.get('REDIS_IP')
if not redis_ip:
    raise Exception()
rd=redis.StrictRedis(host=redis_ip, port=6379, db=0)
rd_plot=redis.StrictRedis(host=redis_ip, port=6379, db=2)

@app.route('/reset', methods=['GET'])
def populate_redis():
    rd.flushdb()
    restaurants = getdata()
    #return restaurants['Restaurants'][(i)]
    for i in range(len(restaurants['Restaurants'])):
        print(restaurants['Restaurants'][(i)])
    #return "done"  
        key="key"+str(i+1)
        rd.hmset(key,restaurants['Restaurants'][(i)])
        #key = ""
    #rd.delete('Restaurants')
    return "Redis Data Reset"+"\n"

@app.route('/create/<key>/<name>/<address>/<zipcode>/<date>/<score>', methods=['GET'])
def create(key, name, address, zipcode, date, score):
    name = name.replace('%', ' ')
    rd.hmset(key, {'Restaurant Name': name, 'Address': address, 'Zip Code': zipcode, 'Date of Inspection': date, 'Inspection Score': score})
    return "New Restaurant: "+str(rd.hgetall(key))+"\n"

@app.route('/read/<key>', methods=['GET'])
def select(key):
    return str(rd.hgetall(key))+"\n"

@app.route('/restaurantlist', methods=['GET'])
def listrestaurants():
    rlist = [rd.hget(key, 'Restaurant Name') for key in rd.keys()]
    return str(rlist)+"\n"

@app.route('/update/<key>/<datapoint>/<new>', methods=['GET'])
def edit_restaurant(key, datapoint, new):
    if datapoint == 'restaurantname':
        new = new.replace('%', ' ')
        rd.hset(key, 'Restaurant Name', new)
    elif datapoint == 'zipcode':
        rd.hset(key, 'Zip Code', new)
    elif datapoint == 'date':
        rd.hset(key, 'Date of Inspection', new)
    elif datapoint == 'score':
        rd.hset(key, 'Inspection Score', new)
    else:
        new = new.replace('%', ' ')
        rd.hset(key, datapoint, new)
    return "Updated Restaurant: "+str(rd.hgetall(key))+"\n"

@app.route('/delete/<key>', methods=['GET'])
def delete(key):
    rd.delete(key)
    return "Entry deleted."+"\n"

@app.route('/emptydb', methods=['GET'])
def emptydb():
    rd.flushdb()
    rd_plot.flushdb()
    return "Databases emptied."+"\n"

@app.route('/jobs', methods=['POST'])
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return "Job submitted."+"\n"+json.dumps(jobs.add_job(job['restaurant']))

@app.route('/download/<restaurant>', methods=['GET'])
def download(restaurant):
    path = f'/app/{restaurant}.png'
    with open(path, 'wb') as f:
        f.write(rd_plot.get((str(restaurant)+'_plot')))
    return send_file(path, mimetype='image/png', as_attachment=True)

def getdata():
    with open("Restaurant_Inspections.json", "r") as json_file:
        userdata = json.load(json_file)
    return userdata

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
