#!/usr/bin/env python
#-*- coding:utf-8 -*-

""" 
Service implementation, inspired by and reusing concepts from the JSONRPC.org python reference implentation
"""

import urllib

try:
    import simplejson as json
except ImportError:
    import json

class JSONRPCClientException(Exception):
    pass

class Client:

    def __init__(self, url, method=None, auth=None):
        self.__url = url
        self.__method = method
        self.__auth = auth
        
    def __getattr__(self, method):
        if self.__method != None:
            method = "%s.%s" % (self.__method, method)
        return Client(self.__url, method, self.__auth)

    def __call__(self, *args):
    
         req = {"jsonrpc": "2.0", "method": self.__method, "params": args, "id": "fixed"}
         
         if self.__auth is not None:
            req["auth"] = self.__auth
         
         postdata = json.dumps(req)
         respdata = urllib.urlopen(self.__url, postdata).read()
         resp = json.loads(unicode(respdata))
         
         if "error" in resp:
             raise JSONRPCClientException(resp["error"]["code"], resp["error"]["message"])
         else:
             return resp["result"]
         

