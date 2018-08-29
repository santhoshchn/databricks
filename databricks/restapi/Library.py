import requests, json


class Library:

    def __init__(self):
        pass

    def install_library(uri, header, libraries, is_library_for_all_clusters=True):
        data = json.dumps(libraries)
        response = requests.post(uri + "libraries/install", data=data, headers=header)
        return Library.__get_details(uri, header, cluster_id=cluster_id)

    def __get_details(uri, header, cluster_id):
        data = json.dumps({"cluster_id": cluster_id})
        response = requests.get(uri + "libraries/all-cluster-statuses", data=data, headers=header)
        return response.json()