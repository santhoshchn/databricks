APE1 = "https://centralus.azuredatabricks.net"
API_VERSION = "2.0"


class Databricks:

    def __init__(self, host, authToken):
        self._host = host
        self._uri = self.__get_uri__(host)
        self._token = authToken
        self._headers = {'Authorization': 'Bearer {0}'.format(self._token)}

    def __get_uri__(self, host):
        return "{host}/api/{api_version}/".format(host=host, api_version=API_VERSION)

    def get_auth_headers(self):
        return self._headers


