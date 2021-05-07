## Installation and Building Image

Github:
git pull git://github.com/colenockolds/COE332-Homework.git/finalProject
#downloads the finalProject repository from Github

To build image:
```
docker build -t colenockolds/nockolds-app:1.0 .
```
To push image:
```
docker push colenockolds/nockolds-app:1.0
```
## Redis Instructions

To create the PVC:
```
kubectl apply -f nockolds-db-pvc.yml
```
Expected output:
```
persistentvolumeclaim/nockolds-db-data created
```
To create the redis deployment:
```
kubectl apply -f nockolds-db-deployment.yml
```
Expected output:
```
deployment.apps/nockolds-db created
```
To create the redis service:
```
kubectl apply -f nockolds-db-service.yml
```
Expected output:
```
service/nockolds-db created
```
## Flask Instructions

To create the flask deployment:
```
kubectl apply -f nockolds-api-deployment.yml
```
Expected output:
```
deployment.apps/nockolds-api created
```
To create the flask service:
```
kubectl apply -f nockolds-api-service.yml
```
Expected output:
```
service/nockolds-api created
```

## Worker and Debug Instructions

To create the worker deployment:
```
kubectl apply -f nockolds-worker-deployment.yml
```
Expected output:
```
deployment.apps/nockolds-worker created
```
To create debug deployment:
```
kubectl apply -f python-debug-deployment.yaml
```
Expected output:
```
deployment.apps/py-debug-deployment created
```
## Checking Work

Once all .yml files have been applied check to make sure everything is running.

To check services:
```
kubectl get services
```
Expected output:
```
NAME                          TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
app1                          NodePort    10.103.86.163    <none>        5000:31014/TCP   30d
nockolds-api                  ClusterIP   10.101.16.98     <none>        5000/TCP         4d
nockolds-db                   ClusterIP   10.99.153.76     <none>        6379/TCP         4d
```
To check pods:
```
kubectl get pods
```
Expected output:
```
NAME                                   READY   STATUS    RESTARTS   AGE
nockolds-api-6f55bc79fb-6w7v4          1/1     Running   0          84m
nockolds-db-7845588-bs6qt              1/1     Running   0          4d
nockolds-worker-69cc7879b-jn29c        1/1     Running   0          84m
py-debug-deployment-5cc8cdd65f-hblm2   1/1     Running   1          23d
```
