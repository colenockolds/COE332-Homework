## Commands to create new deployments:

kubectl apply -f nockolds-hw7-flask-deployment.yml

kubectl apply -f nockolds-hw7-worker-deployment.yml

## Curl Statements and Outputs
```
root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 5}' 10.111.187.154:5000/jobs
{"id": "f2ebf2ea-3e83-4389-ac90-e29f29397b9a", "status": "submitted", "start": 1, "end": 5}

root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 7}' 10.111.187.154:5000/jobs
{"id": "d428a8a0-b1a7-41e4-9b8e-c21da5fb0ea9", "status": "submitted", "start": 1, "end": 7}

root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 2}' 10.111.187.154:5000/jobs
{"id": "c545692f-e5e1-4d2e-8301-3558b85ac64d", "status": "submitted", "start": 1, "end": 2}

root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 4}' 10.111.187.154:5000/jobs
{"id": "e2fa5f2d-dc93-4608-9832-d0507e02d68a", "status": "submitted", "start": 1, "end": 4}

root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 21}' 10.111.187.154:5000/jobs
{"id": "bdb40ba2-8387-42e0-9148-e64c83efa72e", "status": "submitted", "start": 1, "end": 21}

root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 17}' 10.111.187.154:5000/jobs
{"id": "cbc05c9b-939b-41c5-845f-b50a2d1694c4", "status": "submitted", "start": 1, "end": 17}

root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 9}' 10.111.187.154:5000/jobs
{"id": "d058dd98-ef97-423c-bcd4-0f620a36d066", "status": "submitted", "start": 1, "end": 9}

root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 8}' 10.111.187.154:5000/jobs
{"id": "5e5cd46f-9841-4484-b603-4db5582f4561", "status": "submitted", "start": 1, "end": 8}

root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 12}' 10.111.187.154:5000/jobs
{"id": "f5724b81-d060-4ba2-8022-9ef2c44cf830", "status": "submitted", "start": 1, "end": 12}

root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 15}' 10.111.187.154:5000/jobs
{"id": "f0f9859f-e0c3-48be-b2f1-f163618545bb", "status": "submitted", "start": 1, "end": 15}

root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 20}' 10.111.187.154:5000/jobs
{"id": "e3c1d429-80a1-45e3-b9d7-65c79db33954", "status": "submitted", "start": 1, "end": 20}

root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 17}' 10.111.187.154:5000/jobs
{"id": "d979cd27-3e9a-4de8-8be5-b9a40bf117db", "status": "submitted", "start": 1, "end": 17}
```
