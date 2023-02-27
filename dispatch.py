import requests
from uuid import uuid4

def dispatch():
    run_uuid = str(uuid4())
    job_uuid = str(uuid4())
    base = 'https://handler.twoc.semlab-leiden.nl'

    # see https://github.com/FAIRDataTeam/FAIRDataStation/blob/develop/src/main/java/org/fairdatatrain/fairdatastation/api/dto/event/train/TrainDispatchPayloadDTO.java
    payload = {
        'jobUuid': job_uuid,
        'secret': 'foo',
        'callbackEventLocation': f'{base}/runs/{run_uuid}/jobs/{job_uuid}/events',
        'callbackArtifactLocation': f'{base}/runs/{run_uuid}/jobs/{job_uuid}/artifacts',
        'trainUri': 'https://raw.githubusercontent.com/MarekSuchanek/fds-dummy-trains/main/trains/sparql/sparql-train-dashboard.ttl'
    }

    print(f'posting train dispatch with run id {run_uuid} and job id {job_uuid}')
    r = requests.post('https://pgo-2.c4y.fairdatatrain.org/trains', json=payload)
    print(f'response status {r.status_code}, body {r.json()}')

if __name__=='__main__':
    dispatch()
