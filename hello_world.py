#!/usr/bin/python
from flask import Flask
import os
app = Flask(__name__)

@app.route('/tintri')
def hello_world():
	return '0'

if __name__ == "__main__":
	app.run(host='0.0.0.0') 
