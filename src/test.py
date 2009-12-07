from RackSpaceManager import RackSpaceManager
from pprint import pprint

#client = RackSpaceClient(user = '', key = '')
manager = RackSpaceManager()
pprint (manager.ListServers(isDetail = True))
pprint (manager.ListImages(isDetail = True))
