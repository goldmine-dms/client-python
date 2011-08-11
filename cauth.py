#!/usr/bin/env python
#-*- coding:utf-8 -*-

""" Boilerplate client authentication """

import getpass
from gmclient.http_client import Client

service = "http://localhost:8080/service"
client = Client(service)
#username = getpass.getuser()
username = "admin"
#pw = getpass.getpass()
pw = "password"
token = client.authenticate(username, pw)
client = Client(service, auth=token)
