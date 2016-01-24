#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 mapleray <zhiwuliao#gmail.com>
#
# Distributed under terms of the MIT license.
from uuid import uuid4
from base64 import b64encode
from flask import Flask, request
from flask import render_template
from flask import make_response

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/apn", methods=['POST'])
def apn():
    data = {}
    data['name'] = request.form['name']
    data['username'] = request.form['username']
    data['password'] = b64encode(request.form['password'])
    data['proxy_ip'] = request.form['proxy_ip']
    data['port'] = request.form['port']
    data['uuid'] = str(uuid4()).upper()

    resp = make_response(render_template('mobileconfig/apn.mobileconfig',
                                         data=data))
    resp.headers['Content-Disposition'] = 'attachment; filename="apn.mobileconfig"'
    resp.headers['Content-Type'] = 'application/x-apple-aspen-config'
    return resp


if __name__ == "__main__":
    app.debug = True
    app.run()
