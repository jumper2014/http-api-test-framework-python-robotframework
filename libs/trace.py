# coding=utf-8
"""
decorator for debug info
__author__ = 'zengyuetian'
"""

import traceback


def print_trace(function):
    def wrapper(*args, **kw):
        try:
            return function(*args, **kw)
        except Exception, e:
            traceback.print_exc()
            print e.message
            raise e
    return wrapper
