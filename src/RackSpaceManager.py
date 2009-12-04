from RackSpaceClient import RackSpaceClient

class RackSpaceManager:
    def __init__(self, user = '', key = ''):
        self.rsClient = RackSpaceClient(None, None)
    
    def ListServers(self, isDetail = False):
        if isDetail:
            method = "servers/detail"
        else:
            method = "servers"
        servers = self.rsClient.SendRequest(rType = "GET", method = method, params = None )
        return servers

    def ListImages(self, isDetail = False):
        if isDetail:
            method = "images/detail"
        else:
            method = "images"
        images = self.rsClient.SendRequest(rType = "GET", method = method, params = None )
        return images


