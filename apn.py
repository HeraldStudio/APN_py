# -*- coding: utf-8 -*-
import time
import random
from apns import APNs, Frame, Payload
import logging
import requests

import config
import db

# Send multiple notifications in a single transmission
apns = APNs(use_sandbox=True, cert_file='certificate/cert-dev.pem',
	key_file='certificate/key-dev.pem', enhanced=True)


def logger():
	logging.basicConfig(level=logging.DEBUG,
		format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
		datefmt='%a, %d %b %Y %H:%M:%S')
		filename='./log/debug.log',
		filemode='w')

def send(tokens, payload):
	frame = Frame()
	expiry = time.time() + config.expiry
	for token in tokens:
		identifier = random.getrandbits(32)
		frame.add_item(token, payload, identifier, expiry, config.priority)

	apns.gateway_server.register_response_listener(error_handler)
	apns.gateway_server.send_notification_multiple(frame)


def get_pe_info():
	try:
		r = requests.post(config.PE_URL)
		# if r.status_code == 201:
		# 	return
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
		logging.debug("error in get token list at %s" % e)

def error_handler(err):
	print(err)
	logging.debug(err)

def init():
	logger()

def main():
	init()
	try:
		message = get_pe_info()
		tokens = get_token()
		payload = Payload(alert = message, sound = "default", badge = 0)
		send(tokens, payload)
	except Exception,e:
		logging.debug(e)

main()