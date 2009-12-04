from RackSpaceClient import RackSpaceClient
import simplejson

class RackSpaceManager:
# TODO: add exception handling
    def __init__(self, user = '', key = ''):
        self.rsClient = RackSpaceClient(None, None)
    
    def ListServers(self, isDetail = False):
        if isDetail:
            method = "/servers/detail"
        else:
            method = "/servers"
        servers = self.rsClient.SendRequest(rType = "GET", method = method, data = None, params = None )
        return simplejson.loads(servers['body'])

    def ListImages(self, isDetail = False):
        if isDetail:
            method = "/images/detail"
        else:
            method = "/images"
        images = self.rsClient.SendRequest(rType = "GET", method = method, data = None, params = None )
        return simplejson.loads(images['body'])


