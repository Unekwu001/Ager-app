from flask import Flask

ager = Flask(__name__,instance_relative_config=True)
ager.config.from_pyfile('config.py')

from pkg import routes