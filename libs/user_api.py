#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

from libs.const import *
from libs.header import Header
from libs.request import Request
from libs.database import delete_user
from libs.trace import *


@print_trace
def user_create(name, age):
    delete_user(name)
    header = Header()
    header.set_content_json()
    header.set_accept_json()
    body = {"name": name, "age": int(age)}
    req = Request(POST, api_server_host, api_server_port, '/user', header.headers, body)
    resp = req.send()
    return resp