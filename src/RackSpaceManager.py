from RackSpaceClient import RackSpaceClient
from Exceptions import *
import simplejson

class IP:
    def __init__(self):
        self.ip = ""
        self.isPublic = False

class State:
    def __init__(self):
        self.status = ""
        self.progress = 0

class Server:
    def __init__(self):
        # Server id
        self.id = ""

        # Server name
        self.name = ""

        # Additional description
        self.description = ""

        # List of ip addresses
        self.ip = []

        # Server state
        self.state = State()

        # Root password
        self.rootPassword = ""

class ServerImage:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.status = ""
        self.progress = 0
        self.serverId = 0
        self.created = ""
        self.updated = ""

def extractValueOrNone(key, inputDict):
    if isinstance(inputDict, dict):
        return inputDict.get(key, None)
    return None

def parseServer(server, isDetail = False, isPassword = False):
    srv = Server()
    srv.id = server['id']
    srv.name = server['name']
    if isDetail:
        state = State()
        state.status = server.get('status', None)
        state.progress = server.get('progress', None)
        srv.state = state
        # parse IP list
        def parse_ips(addresses, isPublic):
            res = []
            for addr in addresses:
                s_addr = IP()
                s_addr.ip = addr
                s_addr.isPublic = isPublic
                res.append(s_addr)
                return res
        srv.ip.append(parse_ips(server['addresses']['public'], True))
        srv.ip.append(parse_ips(server['addresses']['private'], False))
        if isPassword:
            srv.rootPassword = server['adminPass']
    return srv

def parseImage(img):
    image = ServerImage()
    image.id = img['id']
    image.name = img['name']
    image.serverId = extractValueOrNone("serverId", img)
    image.status = extractValueOrNone("status", img)
    image.progress = extractValueOrNone("progress", img)
    image.created = extractValueOrNone("created", img)
    image.updated = extractValueOrNone("updated", img)
    return image




class RackSpaceManager:
# TODO: add exception handling
    def __init__(self, user = '', key = ''):
        self.rsClient = RackSpaceClient(None, None)
    
    def ListServers(self, isDetail = False):
        if isDetail:
            method = "/servers/detail"
        else:
            method = "/servers"
        servers = self.rsClient.SendRequest(rType = "GET", method = method, data = None, params = None)
        serverList = []
        for server in simplejson.loads(servers['body'])['servers']:
            srv = parseServer(server, isDetail)
            serverList.append(srv)
        return serverList



    def ListImages(self, isDetail = False):
        if isDetail:
            method = "/images/detail"
        else:
            method = "/images"
        images = self.rsClient.SendRequest(rType = "GET", method = method, data = None, params = None)
        imageList = []
        for img in simplejson.loads(images['body'])['images']:
            image = parseImage(img)
            imageList.append(image)
        return imageList

    def CreateServer(self, name, imageId, flavorId, metadata = None, personality = None):
        # Creates server, returns new object or throws exception if something wrong.

        # constructing request
        srv = {"name": name, "imageId": imageId, "flavorId": flavorId}
        if metadata is not None:
            srv["metadata"] = metadata
        if personality is not None:
            srv["personality"] = personality

        req = simplejson.dumps({"server": srv})

        # sending
        try:
            response = self.rsClient.SendRequest(rType="POST", method = "/servers", data = req, params = None)
        except RackSpaceException:
            raise
        # parsing response
# TODO: parse response, handle errors
        if response["code"] == 202:
            server = parseServer(simplejson.loads(response['body'])['server'], True, True)
            return server
        raise RackSpaceException()


    def DeleteServer(self, serverId):
        # Delete specified by id server
        try:
            response = self.rsClient.SendRequest(rType="DELETE", method = "/servers/"+serverId, data = None, params = None)
        except RackSpaceException:
            raise
        if response["code"] != 202:
            # Something wrong
            raise RackSpaceException()

    def UpdateServer(self, serverId, name = None, password = None):
        # Changes server name and root password.
        srv = {}
        if name is not None:
            srv["name"] = name
        if password is not None:
            srv["adminPass"] = password

        request = simplejson.dumps({"server": srv})

        try:
            response = self.rsClient.SendRequest(rType="PUT", method = "/servers/" + serverId, data = request, params = None)
        except RackSpaceException:
            raise
        if response["code"] != 204:
            # Error
            raise RackSpaceException()

    def RebootServer(self, serverId, hardReboot = False):
        # Reboot specified server
        rtype = "SOFT"
        if hardReboot:
            rtype = "HARD"

        req = {"reboot" : {"type": rtype}}
        request = simplejson.dumps(req)

        try:
            response = self.rsClient.SendRequest(rType="POST", method = "/servers/" + serverId + "/action", data = request, params = None)
        except RackSpaceException:
            raise
        if response["code"] != 202:
            # Error
            raise RackSpaceException()

    def CreateImage(self, serverId, name):
        # Create custom image from specified server
        req = {"image" : {"serverId": serverId, "name": name}}
        request = simplejson.dumps(req)

        try:
            response = self.rsClient.SendRequest(rType="POST", method = "/images", data = request, params = None)
        except RackSpaceException:
            raise
        if response["code"] != 202:
            # Error
            raise RackSpaceException()
        image = parseImage(simplejson.loads(response['body'])['image'])
        return image

    def DeleteImage(self, imageId):
        # Delete server image specified by id
        try:
            response = self.rsClient.SendRequest(rType="DELETE", method = "/images/"+imageId, data = None, params = None)
        except RackSpaceException:
            raise
        if response["code"] != 204:
            # Something wrong
            raise RackSpaceException()



