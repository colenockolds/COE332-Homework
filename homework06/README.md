## Installation

Github:
git pull git://github.com/colenockolds/COE332-Homework.git/homework06
#downloads the homework06 repository from Github
 
## Step 1 - Redis PVC
yaml file: nockolds-test-redis-pvc.yaml

command to create PVC: kubectl apply -f nockolds-test-redis-pvc.yaml

output: persistentvolumeclaim/nockolds-redis-data created

## Step 2 - Redis Deployment
yaml file: nockolds-test-redis-deployment.yaml

command to create deployment: kubectl apply -f nockolds-test-redis-deployment.yaml

output: deployment.apps/nockolds-redis-deployment created

## Step 3 - Redis Service
yaml file: nockolds-test-redis-service.yaml

command to create service: apply -f nockolds-test-redis-service.yaml

output: service/nockolds-test-service-redis created

## Checking Work
yaml file: python-debug-deployment.yaml

command to create deployment: kubectl apply -f python-debug-deployment.yaml

output: deployment.apps/py-debug-deployment created

command to find redis service IP: kubectl get services
output:
> NAME                          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE

> app1                          NodePort    10.103.86.163   <none>        5000:31014/TCP   7d9h

> nockolds-test-service-flask   ClusterIP   10.106.48.233   <none>        5000/TCP         147m

> nockolds-test-service-redis   ClusterIP   10.104.203.97   <none>        6379/TCP         163m

commands and outputs for work in debug container:
> [nockolds@isp02 homework06]$ kubectl exec -it py-debug-deployment-5cc8cdd65f-hblm2 -- /bin/bash

> root@py-debug-deployment-5cc8cdd65f-hblm2:/# pip3 install redis

> Requirement already satisfied: redis in /usr/local/lib/python3.9/site-packages (3.5.3)

> root@py-debug-deployment-5cc8cdd65f-hblm2:/# python3

> Python 3.9.4 (default, Apr 10 2021, 15:31:19) 

> [GCC 8.3.0] on linux

> Type "help", "copyright", "credits" or "license" for more information.

> >>> import redis

> >>> rd=redis.StrictRedis(host='10.104.203.97', port=6379, db=0)

> >>> rd.set('key','example')

> True

> >>> rd.keys()

> [b'key']

checking persistence:
1. delete pod
> [nockolds@isp02 homework06]$ kubectl delete pods nockolds-redis-deployment-78b59776f-x459h

> pod "nockolds-redis-deployment-78b59776f-x459h" deleted

2. check that new pod is in list
> [nockolds@isp02 homework06]$ kubectl get pods

> NAME                                              READY   STATUS             RESTARTS   AGE

> nockolds-redis-deployment-78b59776f-6krxw         1/1     Running            0          73s

3. check that key is still present in the debugger:
> >>> rd.keys()

> [b'key']

## Step 4 - Flask Deployment
yaml file: nockolds-test-flask-deployment.yaml

command to create deployment: kubectl apply -f nockolds-test-flask-deployment.yaml

output: deployment.apps/nockolds-test-flask-deployment created

## Step 5 - Flask Service
yaml file: nockolds-test-flask-service.yaml

command to create service: apply -f nockolds-test-flask-service.yaml

output: service/nockolds-test-service-flask created
 
## Final Note
 
I could not get my flask API working correctly, but I decided to leave the REDIS_IP environment variable in the flask deployment yaml file. I also left the files I was using to make an updated version of my API, which include app.py, animals.json, requirements.txt, and dockerfile. 
