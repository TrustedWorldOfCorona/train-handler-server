from flask import Flask, request

app = Flask(__name__)
app.logger.setLevel('INFO')

events = {}
artifacts = {}

@app.route('/runs/<uuid:run_uuid>/events', methods=['POST'])
def receive_job_event(run_uuid: str) -> dict:
    # see https://github.com/FAIRDataTeam/TrainHandler-server/blob/develop/src/main/java/org/fairdatatrain/trainhandler/api/dto/job/JobEventCreateDTO.java
    
    if run_uuid not in events:
        events[run_uuid] = []
    events[run_uuid].append(request.json)

    return request.json

@app.route('/runs/<uuid:run_uuid>/poll/events', methods=['GET'])
def poll_run_events(run_uuid: str) -> [dict]:
    if run_uuid in events:
        return events[run_uuid]
    else:
        return [], 404

@app.route('/runs/<uuid:run_uuid>/artifacts', methods=['POST'])
def receive_job_artifact(run_uuid: str) -> dict:
    # see https://github.com/FAIRDataTeam/TrainHandler-server/blob/develop/src/main/java/org/fairdatatrain/trainhandler/api/dto/job/JobArtifactCreateDTO.java
    
    artifacts[run_uuid] = request.json
    
    return request.json

@app.route('/runs/<uuid:run_uuid>/poll/artifacts', methods=['GET'])
def poll_run_artifact(run_uuid: str) -> dict:
    if run_uuid in artifacts:
        return artifacts[run_uuid]
    else:
        return {}, 404
