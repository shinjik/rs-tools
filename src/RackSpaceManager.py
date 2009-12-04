from RackSpaceClient import RackSpaceClient
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
        serverList = []
        for server in simplejson.loads(servers['body'])['servers']:
            srv = Server()
            srv.id = server['id']
            srv.name = server['name']
            if isDetail:
                state = State()
                state.status = server['status']
                state.progress = server['progress']
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
            serverList.append(srv)
        return serverList



    def ListImages(self, isDetail = False):
        if isDetail:
            method = "/images/detail"
        else:
            method = "/images"
        images = self.rsClient.SendRequest(rType = "GET", method = method, data = None, params = None )
        return simplejson.loads(images['body'])


