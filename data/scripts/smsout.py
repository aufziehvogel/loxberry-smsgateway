import socket
import glob
import time
import os
import requests

UDP_IP = '192.168.1.10'
UDP_PORT = 54875

while True:
	new_files = glob.glob('/var/spool/sms/incoming/*')
	
	time.sleep(1)

	for new_file in new_files:
		from_number = ''
		data_part = False
		msg = ''
		import codecs
		with codecs.open(new_file, 'r', 'iso-8859-15') as f:
			for line in map(unicode.strip, f):
				if line.startswith('From: '):
					from_number = line.replace('From: ', '')
				elif len(line) == 0:
					data_part = True
				elif data_part:
					msg += line

		if msg.startswith('TTS:'):
			try:
				with open('/tmp/sms_permit_numbers') as f:
					allowed_numbers = map(str.strip, f.readlines())
			except IOError:
				allowed_numbers = []

			if from_number in allowed_numbers:
				msg = msg[4:]
				print(msg)
				url = 'http://localhost/loxone/speechout/speechout.php?text=%s&gain=100' % msg
				print(url)
				requests.get(url)
		else:
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			sendmsg = 'Number=%s&Message=%s' % (from_number, msg)
			sock.sendto(sendmsg.encode('utf-8'), (UDP_IP, UDP_PORT))

		os.remove(new_file)
