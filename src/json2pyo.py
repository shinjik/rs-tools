#!/usr/bin/python
from pprint import pprint
import inspect

sdict = {'images': [{'created': '2009-07-20T09:16:57-05:00',
             'id': 2,
             'name': 'CentOS 5.2',
             'status': 'ACTIVE',
             'updated': '2009-07-20T09:16:57-05:00'},
            {'created': '2009-07-20T09:16:57-05:00',
             'id': 3,
             'name': 'Gentoo 2008.0',
             'status': 'ACTIVE',
             'updated': '2009-07-20T09:16:57-05:00'},
            {'created': '2009-07-20T09:16:57-05:00',
             'id': 4,
             'name': 'Debian 5.0 (lenny)',
             'status': 'ACTIVE',
             'updated': '2009-07-20T09:16:57-05:00'},
            {'created': '2009-07-20T09:16:57-05:00',
             'id': 5,
             'name': 'Fedora 10 (Cambridge)',
             'status': 'ACTIVE',
             'updated': '2009-07-20T09:16:57-05:00'},
            {'created': '2009-07-20T09:16:57-05:00',
             'id': 7,
             'name': 'CentOS 5.3',
             'status': 'ACTIVE',
             'updated': '2009-07-20T09:16:57-05:00'},
            {'created': '2009-07-20T09:16:57-05:00',
             'id': 8,
             'name': 'Ubuntu 9.04 (jaunty)',
             'status': 'ACTIVE',
             'updated': '2009-07-20T09:16:57-05:00'},
            {'created': '2009-07-20T09:16:57-05:00',
             'id': 9,
             'name': 'Arch 2009.02',
             'status': 'ACTIVE',
             'updated': '2009-07-20T09:16:57-05:00'},
            {'created': '2009-07-20T09:16:57-05:00',
             'id': 10,
             'name': 'Ubuntu 8.04.2 LTS (hardy)',
             'status': 'ACTIVE',
             'updated': '2009-07-20T09:16:57-05:00'},
            {'created': '2009-07-20T09:16:57-05:00',
             'id': 11,
             'name': 'Ubuntu 8.10 (intrepid)',
             'status': 'ACTIVE',
             'updated': '2009-07-20T09:16:57-05:00'},
            {'created': '2009-07-20T09:16:57-05:00',
             'id': 12,
             'name': 'Red Hat EL 5.3',
             'status': 'ACTIVE',
             'updated': '2009-07-20T09:16:57-05:00'},
            {'created': '2009-07-20T09:16:57-05:00',
             'id': 13,
             'name': 'Fedora 11 (Leonidas)',
             'status': 'ACTIVE',
             'updated': '2009-07-20T09:16:57-05:00'},
            {'id': 14362, 'name': 'Ubuntu 9.10 (karmic)', 'status': 'ACTIVE'},
            {'id': 187811,
             'name': 'CentOS 5.4',
             'status': 'ACTIVE',
             'updated': '2009-11-18T07:39:31-06:00'},
            {'created': '2009-12-01T11:10:29-06:00',
             'id': 189985,
             'name': '05_mpsq_created',
             'progress': 100,
             'serverId': 120210,
             'status': 'ACTIVE',
             'updated': '2009-12-01T11:20:53-06:00'},
            {'created': '2009-12-02T10:38:03-06:00',
             'id': 190255,
             'name': '07_data_imported',
             'progress': 100,
             'serverId': 120210,
             'status': 'ACTIVE',
             'updated': '2009-12-02T10:45:44-06:00'},
            {'created': '2009-12-04T03:24:18-06:00',
             'id': 190765,
             'name': '01_websphere_installed',
             'progress': 100,
             'serverId': 121778,
             'status': 'ACTIVE',
             'updated': '2009-12-04T03:41:07-06:00'},
            {'created': '2009-12-04T08:57:44-06:00',
             'id': 190804,
             'name': '01a_was_installed_no_macys_app',
             'progress': 100,
             'serverId': 121778,
             'status': 'ACTIVE',
             'updated': '2009-12-04T09:17:37-06:00'}]}


class RawMapper:
    class RawClass:
        pass
    
    def foo(self):
        return "FOO!"
   
    aliasMap=None
    
    def __init__(self, inDict, mapHash = None):
        """Base class to map Dict-from-JSON object to Python object"""
        self.resultObject = self.RawClass()
        for i in inDict:
            setattr(self.resultObject, i, inDict[i])
        if mapHash:
            self.setAliasMap(mapHash)
            self.makeAliasMap()

    def setAliasMap(self, mapHash):
        """setAliasMap used to define property aliases
        mapHash is a hash like {'property': 'goto'}
        """
        self.aliasMap = mapHash

    def makeAliasMap(self):
        """makeAliasMap used to map properties to properties"""
        for k in self.aliasMap:
            v = self.aliasMap[k]
            if hasattr(self.resultObject,v):
                setattr(self.resultObject, k, getattr(self.resultObject,v))

    def customMapper(self, propAlias, fn):
        """customMapper will call function to map property to a customMethod"""
        setattr(self.resultObject, propAlias,eval(fn))

    def clearProperty(self, prop):
        """clearProperty used to remap property to smth else"""
        if hasattr(self.resultObject, prop):
            delattr(self.resultObject, prop)

    def getObject(self):
        """getObject pushes RTR object"""
        return self.resultObject



# TEST

rr = []
for it in sdict['images']:
    t = RawMapper(it,{'coolState': 'status', '_ID_': 'id'})
    t.customMapper('foo', 'self.foo()')
    t.clearProperty('updated')
    rr.append(t.getObject())

for tt in rr:
    pprint(inspect.getmembers(tt))

