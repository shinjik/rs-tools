from RackSpaceClient import RackSpaceClient

class RackSpaceManager:
    def __init__(self, user = '', key = ''):
        self.rsClient = RackSpaceClient(None, None)
    def ListServers(self, isDetail = False):
    def ListImages(self):
        images = self.rsClient.SendRequest(rType = "GET", method = "images", params = None )
        return images


