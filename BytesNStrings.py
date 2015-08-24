# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 15:56:55 2015

@author: mjbeck

Collection of str/bytes/unicode conversion tools from Effective Python book
Supports python2  and python3
"""

import sys

#%% Python 3
if sys.version[0] == '3':
    def to_str(bytes_or_str):
        """Takes in bytes or string input and returns it as a str in utf-8"""
        if isinstance(bytes_or_str, bytes):
            #convert to utf-8 str
            value = bytes_or_str.decode('utf-8')
        else:
            value = bytes_or_str
        #return instance of str
        return value

    def to_bytes(bytes_or_str):
        """Takes in bytes or string input and returns it as a bytes"""
        if isinstance(bytes_or_str, str):
            #convert to bytes from utf-8
            value = bytes_or_str.encode('utf-8')
        else:
            value = bytes_or_str
        #return instance of bytes
        return value

#%% Python 2
if sys.version[0] == '2':
    def to_unicode(unicode_or_str):
        """Takes in unicode or str input and returns it as unicode"""
        if isinstance(unicode_or_str, str):
            #convert to str from unicode
            value = unicode_or_str.decode('utf-8')
        else:
            value = unicode_or_str
        #return instance of unicode
        return value

    def to_str(unicode_or_str):
        """Takes in unicode or str input and returns it as str"""
        if isinstance(unicode_or_str, unicode):
            #convert to str from unicode
            value = unicode_or_str.encode('utf-8')
        else:
            value = unicode_or_str
        #return instance of str
        return value
