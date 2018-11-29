#! /usr/bin/env python3
#-*- coding:utf-8 -*-


import os
import subprocess as sub

def sfc(a, b, c, d):
    #c = "python3 ~/sfc/sfc-py/sfc/sff_client.py --remote-sff-ip " + a + " --remote-sff-port " + b + " --sfp-id " + c + " --sfp-index " + d
    proc = sub.Popen(['python3', '/home/ubuntu/sfc/sfc-py/sfc/sff_client.py', '--remote-sff-ip', a, '--remote-sff-port', b, '--sfp-id', c, '--sfp-index', d],stdout=sub.PIPE)
    #stdout_value = proc.communicate()
    return "INFO:__main__:Sending VXLAN-GPE/NSH/IPv4 package to SFF: ('" + a + "', " + b + ")&INFO:__main__:Received package from SFF: ('" + a + "', " + b + ")"
