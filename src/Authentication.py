
# Authentication class, implements basic login and management URL(s) retrieving

from Exceptions import RackSpaceException, RackSpaceAuthenticationFailedException, RackSpaceNotAuthorizedException
import urllib
import urlparse
from httplib  import HTTPSConnection, HTTPConnection, HTTPException
import ConfigParser
import os
#from utils    import parse_url

class Authentication:
    # API login, should be provided or get from .rackspacerc file (by default)
    api_user = None

    # API key, should be provided or get from .rackspacerc file (by default)
    api_key = None

    # Auth token will be returned if authentication  was successeful
    auth_token = None

    # Server management URL is given as response to auth request
    api_url = None
    auth_url = "https://auth.api.rackspacecloud.com/v1.0"

    def __init__(self, user, key, url = None):
        # try to get auth info from params
        if user != "":
            self.api_user = user
        if key != "":
            self.api_key = key
        if url is not None:
            self.auth_url = url


        # if no params specified, read from config
        if self.api_key is None or self.api_user is None:
            config = ConfigParser.ConfigParser()
            config.read(os.path.expanduser("~/.rackspacerc"))
            if not config.has_section('account'):
                print "No such account defined in config file!"
                sys.exit(1)
            self.api_user = config.get('account', 'username')
            self.api_key = config.get('account', 'secret')


    def doLogin(self):
        """ Perform login, raise exception if something wrong """
        self.api_url = None
        self.auth_token = None
        uri = urlparse.urlparse(self.auth_url)
        headers = dict()
        headers['x-auth-user'] = self.api_user
        headers['x-auth-key'] = self.api_key

        conn = HTTPSConnection(uri.hostname, uri.port)
        conn.request('GET', self.auth_url, '', headers)
        response = conn.getresponse()
        buff = response.read()

        # 401 == Auth failed
        if response.status == 401:
            raise RackSpaceAuthenticationFailedException()

        # TODO: check codes and return more informative exceptions
        if response.status != 204:
            raise RackSpaceException()

        for header in response.getheaders():
            if header[0].lower() == "x-server-management-url":
                self.api_url = header[1]
            if header[0].lower() == "x-auth-token":
                self.auth_token = header[1]

        conn.close()

        if self.auth_token is None or self.api_url is None:
            # Invalid response
            raise RackSpaceException()


    def getServerManagementURL(self):
        if self.api_url is not None:
            return self.api_url
        else:
            raise RackSpaceNotAuthorizedException()

    def getAuthToken(self):
        if self.auth_token is not None:
            return self.auth_token
        else:
            raise RackSpaceNotAuthorizedException()


