import time
from apns import APNs, Frame, Payload
import logging
import requests

import config
import db

# Send a single notification
# apns = APNs(use_sandbox=True, cert_file='cert.pem', key_file='key.pem')
# apns.gateway_server.send_notification(token_hex, payload)

# Send multiple notifications in a single transmission
apns = APNs(use_sandbox=True, cert_file='apns.pem', enhanced=True)


def logger():
	logging.basicConfig(level=logging.DEBUG,
		format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
		datefmt='%a, %d %b %Y %H:%M:%S',
		filename='./log/db.log',
		filemode='w')

def send(tokens, payload):
	frame = Frame()
	for token in tokens:
		frame.add_item(token, payload, config.identifier,
			time.time()+config.expiry, config.priority)

	apns.gateway_server.register_response_listener(error_handler)
	apns.gateway_server.send_notification_multiple(frame)


def get_pe_info():
	try:
		r = requests.post(PE_URL)
		result = r.json()
		pe_info = result.get('content')
		if pe_info:
			return pe_info
		else:
			raise Exception('no content in json result')
	except Exception, e:
		logging.error("error in request pe info at %s" % e)

		
def get_token():
	try:
		result = db.get_token_list()
		return result
	except Exception,e:
		logging.dubug("error in get token list at %s" % e)

def error_handler(err):
	logging.debug(err)

def main():
	try:
		message = get_pe_info()
		tokens = get_token()
		payload = Payload(alert=message, sound="default", badge=1)
		send(tokens, payload)

	except Exception,e:
		logging.dubug(e)

# main()