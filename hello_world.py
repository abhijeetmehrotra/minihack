#!/usr/bin/python
from flask import Flask
import os
app = Flask(__name__)

@app.route('/tintri')
def hello_world():
	val = os.environ.get('RETVAL')
	if val:
		return str(val)
	else:
		return '2'

if __name__ == "__main__":
	app.run(host='0.0.0.0') 