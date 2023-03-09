import requests
from uuid import uuid4

def dispatch():
    run_uuid = str(uuid4())
    base = 'https://handler.twoc.semlab-leiden.nl'

    # see https://github.com/FAIRDataTeam/FAIRDataStation/blob/develop/src/main/java/org/fairdatatrain/fairdatastation/api/dto/event/train/TrainDispatchPayloadDTO.java
    payload = {
        'jobUuid': run_uuid,
        'secret': 'foo',
        'callbackEventLocation': f'{base}/runs/{run_uuid}/events',
        'callbackArtifactLocation': f'{base}/runs/{run_uuid}/artifacts',
        'trainUri': 'https://raw.githubusercontent.com/MarekSuchanek/fds-dummy-trains/main/trains/sparql/sparql-train-dashboard.ttl'
    }

    print(f'posting train dispatch with run id {run_uuid}')

    print(f'curl {base}/runs/{run_uuid}/poll/events')
    print(f'curl {base}/runs/{run_uuid}/poll/artifacts')

    r = requests.post('https://pgo-2.c4y.fairdatatrain.org/trains', json=payload)
    print(f'response status {r.status_code}, body {r.json()}')

if __name__=='__main__':
    dispatch()
