from RackSpaceClient import RackSpaceClient

client = RackSpaceClient(user = '', key = '')
res = client.SendRequest('GET', '/servers', '', None)
print res['code']
print res['body']
