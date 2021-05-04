import json
import redis
from flask import Flask, request
import os
import jobs

app = Flask(__name__)

redis_ip = os.environ.get('REDIS_IP')
if not redis_ip:
    raise Exception()
rd=redis.StrictRedis(host=redis_ip, port=6379, db=0)

@app.route('/reset', methods=['GET'])
def populate_redis():
    rd.flushdb()
    restaurants = getdata()
    for i in range(len(restaurants['Restaurants'])):
        key="key"+str(i+1)
        rd.hmset(key,restaurants['Restaurants'][(i)])
        key = ""
    rd.delete('Restaurants')
    return key+"\n"

@app.route('/jobs', methods=['POST'])
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return json.dumps(jobs.add_job(job['start'], job['end']))

def getdata():
    with open("Restaurant_Inspections.json", "r") as json_file:
        userdata = json.load(json_file)
    return userdata

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
