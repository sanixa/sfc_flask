#! /usr/bin/env python3
#-*- coding:utf-8 -*-

import func

from flask import Flask
from flask import request
from flask import session
from flask import jsonify

app = Flask(__name__)

@app.route('/sfc/',methods=['GET','POST'])
def sfc():
    sff_ip = str(request.args.get('a'))
    sff_port = str(request.args.get('b'))
    sfc_id = str(request.args.get('c'))
    sfc_index = str(request.args.get('d'))
    
    return func.sfc(sff_ip, sff_port, sfc_id, sfc_index)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

