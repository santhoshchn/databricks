import json, requests 

class Cluster:

    def __init__(self, uri, header):
        self.uri = uri
        self.header = header

    def create_cluster(self, cluster_details):
        response = requests.post(self.uri + "clusters/create", data=json.dumps(cluster_details), headers=self.header)
        return response.json()

    def get_cluster_details(self, cluster_id):
        response = requests.get(self.uri + "clusters/get", data=json.dumps({"cluster_id": cluster_id}), headers=self.header)
        return response.json()



