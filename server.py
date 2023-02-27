from flask import Flask, request
from base64 import b64decode

app = Flask(__name__)
app.logger.setLevel('INFO')

@app.route('/runs/<uuid:run_uuid>/jobs/<uuid:job_uuid>/events', methods=['POST'])
def receive_job_event(run_uuid: str, job_uuid: str) -> dict:
    # see https://github.com/FAIRDataTeam/TrainHandler-server/blob/develop/src/main/java/org/fairdatatrain/trainhandler/api/dto/job/JobEventCreateDTO.java
    body = request.json
    #body['resultStatus']
    #body['message']
    #body['occuredAt']
    #body['remoteId']
    #body['secret']
    app.logger.info(f'got event: {request.json}')
    return request.json

@app.route('/runs/<uuid:run_uuid>/jobs/<uuid:job_uuid>/artifacts', methods=['POST'])
def receive_job_artifact(run_uuid: str, job_uuid: str) -> dict:
    # see https://github.com/FAIRDataTeam/TrainHandler-server/blob/develop/src/main/java/org/fairdatatrain/trainhandler/api/dto/job/JobArtifactCreateDTO.java
    body = request.json
    #body['displayName']
    #body['fileName']
    #body['hash']
    #body['bytesize']
    #body['contentType']
    #body['occuredAt']
    #body['remoteId']
    #body['secret']
    #body['base64data']
    app.logger.info(f'got artifact: {request.json}')
    app.logger.info(b64decode(body['base64data']))
    return request.json
