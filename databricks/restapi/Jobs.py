import requests, json, time, traceback


class Jobs:

    def __init__(self, uri, header):
        self.uri = uri
        self.header = header
        
    def __create_job(self, job):
        response = requests.post(url=self.uri + "jobs/create", headers=self.header, data=json.dumps(job))
        response.json()

    def run_submit(self, job):
        response = requests.post(url=self.uri + "jobs/runs/submit", headers=self.header, data=json.dumps(job))
        response.json()

    def __get_job_status(self, run_id):
        response=requests.get(url=self.uri + "jobs/runs/get", headers=self.header, data=json.dumps({"run_id": run_id}))
        return response.json()

