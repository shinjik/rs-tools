from Authentication import Authentication
from Exceptions import *

class RackSpaceClient:

    # Authentication object
    auth = None

    # Default headers
    headers = {'Content-Type' : 'application/xml',
                'Accept' : 'application/xml'}

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
        self.headers.update({ 'X-Auth-Token' : self.auth.getAuthToken() })
        print self.headers



    def SendRequest(self, rType, method, params):
# Send API request
# 200 or 203 is normal codes of response
# TODO: support reconnect

        return None

