#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


def verify_status_code(response, expected_status_code):
    try:
        print "Real status code:   ", response.status_code
        print "Expected status code: ", expected_status_code
        if str(response.status_code) != str(expected_status_code):
                raise AssertionError('http request response is: %s\n'
                                     'expected: %s'
                                     % (response.status_code, expected_status_code))
    except Exception as err:
        raise AssertionError('Verify status code fail:\n%s' % err)