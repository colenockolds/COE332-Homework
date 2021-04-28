## Commands to create new deployments:

kubectl apply -f nockolds-hw7-flask-deployment.yml

kubectl apply -f nockolds-hw7-worker-deployment.yml

## Curl Statements and Outputs
```
root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 5}' 10.111.187.154:5000/jobs
{"id": "f2ebf2ea-3e83-4389-ac90-e29f29397b9a", "status": "submitted", "start": 1, "end": 5}
```
```
root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 7}' 10.111.187.154:5000/jobs
{"id": "d428a8a0-b1a7-41e4-9b8e-c21da5fb0ea9", "status": "submitted", "start": 1, "end": 7}
```
