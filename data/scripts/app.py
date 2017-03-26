import flask
import subprocess
import threading
import time
import uuid
import codecs

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
