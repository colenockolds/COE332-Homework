import json
import redis
import datetime
import os
from flask import Flask, request

app = Flask(__name__)

redis_ip = os.environ.get('REDIS_IP')
if not redis_ip:
    raise Exception()
rd=redis.StrictRedis(host=redis_ip, port=6379, db=0)

@app.route('/animals', methods=['GET'])
def get_animals():
        animal_list = ""
        for i in range(rd.dbsize()):
            key="key"+str(i+1)
            animal_list = animal_list+str(rd.hgetall(key))
        return animal_list+"\n"

@app.route('/animals/count', methods=['GET'])
def count_animals():
    return str(rd.dbsize())+"\n"

@app.route('/animals/dates', methods=['GET'])
def select_dates():
    date1 = request.args.get('d1')
    date2 = request.args.get('d2')
    date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    within_range = ""
    for i in range(rd.dbsize()):
        key="key"+str(i+1)
        date_created = str(rd.hmget(key, 'created_on'))
        date_created = date_created.replace('[', '')
        date_created = date_created.replace("'", '')
        date_created = date_created.replace(']', '')
        date_created = datetime.datetime.strptime(date_created, "%Y-%m-%d")
        if date1 <= date_created and date_created <= date2:
            within_range = within_range+str(rd.hgetall(key))
        if i == 19:
            return "All animals created within the queried date range: "+within_range+"\n"

@app.route('/animals/dates/remove', methods=['GET'])
def remove_animals_by_date():
    date1 = request.args.get('d1')
    date2 = request.args.get('d2')
    date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    within_range = ""
    for i in range(rd.dbsize()):
        key="key"+str(i+1)
        date_created = str(rd.hmget(key, 'created_on'))
        date_created = date_created.replace('[', '')
        date_created = date_created.replace("'", '')
        date_created = date_created.replace(']', '')
        date_created = datetime.datetime.strptime(date_created, "%Y-%m-%d")
        if date1 <= date_created and date_created <= date2:
            rd.delete(key)
        if i == 19:
            return within_range+"\n"

@app.route('/animals/average_legs', methods=['GET'])
def average_legs():
    total_legs = 0.0
    if rd.dbsize() == 0:
        return "There are no animals!\n"
    for i in range(rd.dbsize()):
        key="key"+str(i+1)
        legs = str(rd.hmget(key, 'legs'))
        legs = legs.replace('[', '')
        legs = legs.replace("'", '')
        legs = legs.replace(']', '')
        total_legs = total_legs + float(legs)
    return str(total_legs/rd.dbsize())+"\n"

@app.route('/reset', methods=['GET'])
def populate_redis():
    animals = getdata()
    for i in range(len(animals['animals'])):
        key="key"+str(i+1)
        rd.delete(key)
        rd.hmset(key,animals['animals'][(i)])
        key = ""
    rd.delete('animals')
    return key+"\n"

@app.route('/animals/select/<UUID>', methods=['GET'])
def select(UUID):
    UUID = "['"+str(UUID)+"']"
    for i in range(rd.dbsize()):
        key = "key"+str(i+1)
        uid = str(rd.hmget(key, 'uid'))
        if uid == UUID:
            return str(rd.hgetall(key))+"\n"
        
@app.route('/animals/edit/<UUID>/<bodypart>/<new>', methods=['GET'])
def edit_animal(UUID, bodypart, new):
    UUID = "['"+str(UUID)+"']"
    for i in range(rd.dbsize()):
        key = "key"+str(i+1)
        uid = str(rd.hmget(key, 'uid'))
        if uid == UUID:
            bodypart = str(bodypart)
            rd.hset(key, bodypart, new)
            return "Edited Animal: "+str(rd.hgetall(key))+"\n"

@app.route('/print', methods=['GET'])
def print_redis_data():
    return str(rd.keys())+"\n"
    
def getdata():
    with open("animals.json", "r") as json_file:
        userdata = json.load(json_file)
    return userdata

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
