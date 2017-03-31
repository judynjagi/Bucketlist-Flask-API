from .bucketlist import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from configsettings.config import config

db = SQLAlchemy()

def create_app(configuration):
	app = Flask(__name__)
	app.config.from_object(config[configuration])
	db.app = app
	db.init_app(app)

	return app

app = create_app("development")
api = Api(app=app)
