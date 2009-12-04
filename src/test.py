from RackSpaceManager import RackSpaceManager

#client = RackSpaceClient(user = '', key = '')
manager = RackSpaceManager()
print manager.ListServers(isDetail = True)
print manager.ListImages(isDetail = True)
