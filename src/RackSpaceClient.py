from Authentication import Authentication
from Exceptions import *
import urlparse
from httplib  import HTTPSConnection, HTTPConnection, HTTPException


class RackSpaceClient:
    VALID_HTTP_METHODS = ('GET', 'POST', 'DELETE')

    # Authentication object
    auth = None

    # Default headers
    headers = {'Content-Type' : 'application/json',
                'Accept' : 'application/json'}

    connection = None

    def __init__(self, user, key):
        self.auth = Authentication(user, key)
        try:
            self.auth.doLogin()
        except RackSpaceAuthenticationFailedException:
            print "Invalid credentials was provided!"
            self.auth = None
        except RackSpaceException:
            print "Error during auth procedure"
            #sys.exit(1)
            self.auth = None
        self.updateAuthToken(self.auth.getAuthToken())
        #print self.headers

    def updateAuthToken(self, token):
        self.headers.update({ 'X-Auth-Token' : token })

    def makeConnection(self, hostname, port):
        self.closeConnection()
        self.connection = HTTPSConnection(hostname, port)

    def closeConnection(self):
        if self.connection is not None:
            self.connection.close()





    def SendRequest(self, rType, method, data, params):
        # Send API request

        if rType not in self.VALID_HTTP_METHODS:
            # Invalid request method
            raise RackSpaceException()

        uri = urlparse.urlparse(self.auth.getServerManagementURL())

        headers = self.headers.copy()
        if isinstance(params, dict):
            headers.update(params)

        def make_request():
            self.makeConnection(uri.hostname, uri.port)
            self.connection.request(rType, self.auth.getServerManagementURL() + method, data, headers)
            resp = self.connection.getresponse()
            return resp

        response = make_request()

        # 401 == unauthorized
        if response.status == 401:
            try:
                self.auth.doLogin()
                # retry request
                response = make_request()
            except RackSpaceException:
                self.closeConnection()
                raise

#        if response.status == 413:
#            raise RackSpaceOverLimitException()
#        if response.status == 400 or response.status == 500:
#            raise RackSpaceCloudServersFaultException()
#        if response.status == 503:
#            raise RackSpaceServiceUnavailableException()

        result = { "code" : response.status, "body" : response.read() }
        self.closeConnection()


        return result

