## Commands to create new deployments:

kubectl apply -f nockolds-hw7-flask-deployment.yml

kubectl apply -f nockolds-hw7-worker-deployment.yml

## Curl Statements and Outputs
```
root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 5}' 10.111.187.154:5000/jobs
{"id": "6dbe522f-ca44-443c-9e6b-fc28d0dd5e3e", "status": "submitted", "start": 1, "end": 5}
root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 5}' 10.111.187.154:5000/jobs
{"id": "65402f88-c275-4ff1-aca1-1859eaa7d5dd", "status": "submitted", "start": 1, "end": 5}
root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 5}' 10.111.187.154:5000/jobs
{"id": "e3e49b42-61d9-494d-bf9b-5e4d016a4871", "status": "submitted", "start": 1, "end": 5}
root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 5}' 10.111.187.154:5000/jobs
{"id": "fbcb8fd4-a8ca-4675-bed2-b85d6e111a00", "status": "submitted", "start": 1, "end": 5}
root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 5}' 10.111.187.154:5000/jobs
{"id": "99e3f5b3-8d51-459f-807f-80a823ffdd23", "status": "submitted", "start": 1, "end": 5}
root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 5}' 10.111.187.154:5000/jobs
{"id": "25b8168e-e437-453f-aace-3176edfbada4", "status": "submitted", "start": 1, "end": 5}
root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 5}' 10.111.187.154:5000/jobs
{"id": "aa91360e-f9f6-43fd-b5a5-63c25543740c", "status": "submitted", "start": 1, "end": 5}
root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 5}' 10.111.187.154:5000/jobs
{"id": "0550c07a-5896-48c2-a3a2-f4c4e57f653f", "status": "submitted", "start": 1, "end": 5}
root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 5}' 10.111.187.154:5000/jobs
{"id": "bbd951ce-ee4c-451f-95db-f23fe4006c2a", "status": "submitted", "start": 1, "end": 5}
root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 5}' 10.111.187.154:5000/jobs
{"id": "7109e5a1-ca85-4f6f-8003-312733566df8", "status": "submitted", "start": 1, "end": 5}
root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 5}' 10.111.187.154:5000/jobs
{"id": "84a05cdd-6655-4153-9b9d-cb83b42cc4b3", "status": "submitted", "start": 1, "end": 5}
root@py-debug-deployment-5cc8cdd65f-hblm2:/# curl -X POST -H "content-type: application/json" -d '{"start": 1, "end": 5}' 10.111.187.154:5000/jobs
{"id": "18284734-567b-4976-9e18-71faab83a2e3", "status": "submitted", "start": 1, "end": 5}
```

## Checking Job Status 
```
>>> rd.hgetall(b'job.e3e49b42-61d9-494d-bf9b-5e4d016a4871')
{b'id': b'e3e49b42-61d9-494d-bf9b-5e4d016a4871', b'status': b'complete', b'start': b'1', b'end': b'5', b'IP': b'10.244.12.100'}
>>> rd.hgetall(b'job.6dbe522f-ca44-443c-9e6b-fc28d0dd5e3e')
{b'id': b'6dbe522f-ca44-443c-9e6b-fc28d0dd5e3e', b'status': b'complete', b'start': b'1', b'end': b'5', b'IP': b'10.244.12.100'}
>>> rd.hgetall(b'job.0550c07a-5896-48c2-a3a2-f4c4e57f653f')
{b'id': b'0550c07a-5896-48c2-a3a2-f4c4e57f653f', b'status': b'complete', b'start': b'1', b'end': b'5', b'IP': b'10.244.10.196'}
>>> rd.hgetall(b'job.aa91360e-f9f6-43fd-b5a5-63c25543740c')
{b'id': b'aa91360e-f9f6-43fd-b5a5-63c25543740c', b'status': b'complete', b'start': b'1', b'end': b'5', b'IP': b'10.244.12.100'}
>>> rd.hgetall(b'job.fbcb8fd4-a8ca-4675-bed2-b85d6e111a00')
{b'id': b'fbcb8fd4-a8ca-4675-bed2-b85d6e111a00', b'status': b'complete', b'start': b'1', b'end': b'5', b'IP': b'10.244.10.196'}
>>> rd.hgetall(b'job.18284734-567b-4976-9e18-71faab83a2e3')
{b'id': b'18284734-567b-4976-9e18-71faab83a2e3', b'status': b'complete', b'start': b'1', b'end': b'5', b'IP': b'10.244.10.196'}
>>> rd.hgetall(b'job.99e3f5b3-8d51-459f-807f-80a823ffdd23')
{b'id': b'99e3f5b3-8d51-459f-807f-80a823ffdd23', b'status': b'complete', b'start': b'1', b'end': b'5', b'IP': b'10.244.12.100'}
>>> rd.hgetall(b'job.25b8168e-e437-453f-aace-3176edfbada4')
{b'id': b'25b8168e-e437-453f-aace-3176edfbada4', b'status': b'complete', b'start': b'1', b'end': b'5', b'IP': b'10.244.10.196'}
>>> rd.hgetall(b'job.84a05cdd-6655-4153-9b9d-cb83b42cc4b3')
{b'id': b'84a05cdd-6655-4153-9b9d-cb83b42cc4b3', b'status': b'complete', b'start': b'1', b'end': b'5', b'IP': b'10.244.12.100'}
>>> rd.hgetall(b'job.65402f88-c275-4ff1-aca1-1859eaa7d5dd')
{b'id': b'65402f88-c275-4ff1-aca1-1859eaa7d5dd', b'status': b'complete', b'start': b'1', b'end': b'5', b'IP': b'10.244.10.196'}
>>> rd.hgetall(b'job.7109e5a1-ca85-4f6f-8003-312733566df8')
{b'id': b'7109e5a1-ca85-4f6f-8003-312733566df8', b'status': b'complete', b'start': b'1', b'end': b'5', b'IP': b'10.244.10.196'}
>>> rd.hgetall(b'job.bbd951ce-ee4c-451f-95db-f23fe4006c2a')
{b'id': b'bbd951ce-ee4c-451f-95db-f23fe4006c2a', b'status': b'complete', b'start': b'1', b'end': b'5', b'IP': b'10.244.12.100'}
```
