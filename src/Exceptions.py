# RackSpace exceptions

class RackSpaceException(Exception): pass
class RackSpaceAuthenticationFailedException(RackSpaceException): pass
class RackSpaceNotAuthorizedException(RackSpaceException): pass
class RackSpaceCloudServersFaultException(RackSpaceException): pass
class RackSpaceOverLimitException(RackSpaceException): pass
class RackSpaceBadRequestException(RackSpaceException): pass
class RackSpaceServiceUnavailableException(RackSpaceException): pass

