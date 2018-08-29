import requests, json

TOKEN="token/"


class Token:

    def __init__(self, databricks):
        self.databricks = databricks

    def generate_new_token(self, comments, lifetime_seconds=7776000):
        data = json.dumps({"comments": comments, "lifetime_seconds":lifetime_seconds})
        response = requests.post(url=self.databricks._uri + TOKEN + "create", data=data, headers=self.databricks.get_auth_headers())
        return response.json()
