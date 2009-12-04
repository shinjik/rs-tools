from Authentication import Authentication

auth = Authentication(user='', key='')
auth.doLogin()
print "auth successful, management url is: ['%s'], api key is " % auth.getServerManagementURL(), auth.getAuthToken()



