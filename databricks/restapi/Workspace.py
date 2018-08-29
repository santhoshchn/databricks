import requests, json, base64


class Workspace:

    def __init__(self):
        pass

    def create_directory(uri, header, folder_name):
        response = requests.post(url=uri + "workspace/mkdirs", headers=header, data=json.dumps({"path": folder_name}))
        return response.json()

    def get_object_details(uri, header, path):
        response = requests.get(url=uri + "workspace/get-status", headers=header, data=json.dumps({"path":path}))
        return response.json()

    def import_notebook(uri, header, databricks_import_path, local_path, notebook_language="PYTHON", overwrite=False, format="SOURCE"):

        with open(local_path, 'rb') as notebook:
            notebook_bytes = notebook.read()
        notebookBytesEncoded = (base64.b64encode(notebook_bytes)).decode("utf-8")
        import_request_content = {"content": notebookBytesEncoded, "path": databricks_import_path, "language": notebook_language, "overwrite": overwrite, \
                                  "format": format}
        response = requests.post(url=uri + "workspace/import", headers=header, data=json.dumps(import_request_content))
        return response.json()
        
    def delete(uri, header, path, recursive):
        response = requests.get(uri=uri, headers=header, data=json.dumps({"path": path, "recursive": recursive}))
        return response.json()
