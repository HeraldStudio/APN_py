from flask import Flask, abort, send_file

import config
import db

app = Flask(__name__)

@app.route('/')
def index():
    abort(404)

@app.route('/apn/<token>', methods=['POST'])
def apn(token):
	length = len(token)
	if (length != 64):
		db.set_token(token)
		flask.Response(status=200)
	else:
		abort(403)

@app.route('/update/<version>', methods=['GET', 'POST'])
def update(version):
	try:
		client_version = float(version)
	except Exception, e:
		return abort(403)
	if (client_version < config.api_version):
		return send_file('./api/APIList.plist', mimetype='text/xml')
	else:
		return flask.Response(status=304)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)