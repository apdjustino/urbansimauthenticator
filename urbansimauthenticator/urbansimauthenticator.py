from jupyterhub.auth import Authenticator
from tornado import gen
import requests
import json


class UrbanSimAuthenticator(Authenticator):

    @gen.coroutine
    def authenticate(self, handler, data):
        credentials = {'user': data['username'], 'pass': data['password']}
        r = requests.post('http://test.urbansim.com/api/users/login', data=credentials)
        response = json.loads(r.content)
        if 'token' in response:
            return data['username']
        else:
            return None
