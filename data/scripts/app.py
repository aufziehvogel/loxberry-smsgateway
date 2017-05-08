import flask
import subprocess
import threading
import time
import uuid
import codecs
import os.path
import re

app = flask.Flask(__name__)

@app.route('/send_sms')
def send_sms():
	number = flask.request.args.get('number')
	message = flask.request.args.get('message')

	filename = str(uuid.uuid4())
	with codecs.open('/var/spool/sms/outgoing/%s' % filename, 'w', 'iso-8859-15') as f:
		f.write('To: %s\n' % number)
		f.write('\n')
		f.write(message)

@app.route('/voice_call')
def voice_call():
	# Make sure that users only input numbers or + as input, but
	# allow leading zeroes
	number = re.sub('[^+\d]', '', flask.request.args.get('number'))
	duration = int(flask.request.args.get('duration'))

	subprocess.call(['/etc/init.d/smstools', 'stop'])
	
	curdir = os.path.dirname(os.path.realpath(__file__))
	bash_script = os.path.join(curdir, 'voice_call.sh')
	#print('bash %s %s %d' % (bash_script, number, duration))
	subprocess.call('bash %s %s %d' % (bash_script, number, duration), shell=True)
	
	subprocess.call(['/etc/init.d/smstools', 'start'])

@app.route('/number/<int:number>')
def permit_sms_number(number):
	with open('/tmp/sms_permit_numbers', 'a+') as f:
		lines = map(str.strip, f.readlines())
		if not str(number) in lines:
			f.write(str(number) + '\n')

@app.route('/delete_numbers')
def delete_sms_numbers():
	try:
		os.remove('/tmp/sms_permit_numbers')
	except:
		pass
