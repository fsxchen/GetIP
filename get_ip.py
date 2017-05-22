#!/usr/bin/env python
# -*- coding:utf-8 -*- 
'''
File Name: get_ip.py
Description: 
Created_Time: 2017-05-22 11:27:58
Last modified: 2017-05-22 13时25分26秒
'''

_author = 'arron'
_email = 'fsxchen@gmail.com'

APNIC_URL = "ftp://ftp.apnic.net/public/apnic/stats/apnic/delegated-apnic-latest"


import os

from urllib import request
from datetime import datetime
import math
import socket

today = datetime.now().strftime("%y-%m-%d")
local_file = "local_file_%s.txt" % today


def get_apnic_file():
    if os.path.isfile(local_file):
        return True
    else:
        try:
            ips = request.urlopen(APNIC_URL).read()
            with open(local_file, "w") as fd:
                fd.write(ips.decode("utf-8"))
                return True
        except Exception as e:
            return False

def get_ip_list(cny="CN", ver="ipv4"):
    if get_apnic_file():
        with open(local_file, "r") as fd:
            for line in fd:
                tl = line.strip().split("|")
                if len(tl) >3 and tl[1] == cny and tl[2] == ver:
                    ip_start = tl[3]
                    ip_mask = 32 - int(math.log(int(tl[4]), 2)) 
                    print("%s/%d" % (ip_start, ip_mask))

if __name__ == "__main__":

    get_ip_list()
    
