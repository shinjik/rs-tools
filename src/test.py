
from Authentication import Authentication

auth = Authentication(user='kishanov', key='a7a97224659b2d68a7c3efe969583744')
auth.doLogin()
print "auth successful, management url is: ['%s'], api key is " % auth.getServerManagementURL(), auth.getAuthToken()



