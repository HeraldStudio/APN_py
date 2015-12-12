# -*- coding: utf-8 -*-
from flask import *

import config
import db

app = Flask(__name__)

@app.route('/')
def index():
    abort(404)

@app.route('/apn/reg', methods=['POST'])
def apn_reg():
	token = request.form['token']
	try:
		length = len(token)
		if (length == 64):
			db.set_token(token)
			return ("success", 200)
		else:
			abort(403)
	except Exception, e:
		abort(500)

@app.route('/apn/remove', methods=['POST'])
def apn_remove():
	token = request.form['token']
	try:
		length = len(token)
		if (length == 64):
			db.remove_token(token)
			return ("success", 200)
		else:
			abort(403)
	except Exception, e:
		abort(500)

@app.route('/update', methods=['GET'])
def update():
	version = request.args.get('version')
	try:
		client_version = float(version)
	except Exception, e:
		return abort(403)
	if (client_version < config.api_version):
		return send_file('./api/APIList.plist')
	else:
		return ("latest", 304)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)