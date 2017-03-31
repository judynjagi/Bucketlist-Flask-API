from datetime import datetime

from flask_migrate import Migrate
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
						  as Serializer, BadSignature, SignatureExpired)
from sqlalchemy.orm import validates

from bucketlist import app, db

class Users(db.Model):
	__tablename__ = 'users'

	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(250), nullable=False)
	password_hash = db.Column(db.String(64), nullable=False)
	email= db.Column(db.String(250), nullable=False, unique=True)


	def hash_password(self, password):
		self.password_hash = pwd_context.encrypt(password)
		self.verify_password_hash = pwd_context.encrypt(password)

	def verify_password(self, password):
		return pwd_context.verify(password, self.password_hash)

	def generate_auth_token(self, expiration=36000):
		"""Expires in 36 minutes"""
		S = Serializer('SECRET_KEY', expires_in=expiration)
		return S.dumps({'user_id': self.user_id})

	@validates('email', include_removes=True)
	def validate_email(self, key, users, is_remove):
		assert '@' in users
		return users
			
	@staticmethod
	def verify_auth_token(token):
		s = Serializer('SECRET_KEY')
		try:
			data = s.loads(token)
		except SignatureExpired:
			return None
		except BadSignature:
			return None
		user = Users.query.get(data['user_id'])
		return user

	def __repr__(self):
		return "<Users: %r>" % self.username

class BucketList(db.Model):

	"""docstring for ClassName"""
	__tablename__ = 'bucketlist'

	list_id = db.Column(db.Integer, primary_key=True)
	list_title = db.Column(db.String(255))
	list_description = db.Column(db.Text)
	date_created = db.Column(db.DateTime, default=datetime.now)
	date_modified = db.Column(db.DateTime, onupdate=datetime.now)
	# This Value is constrained to be  the one of the remote column which is user.id (PK)
	created_by = db.Column(db.Integer, db.ForeignKey("users.user_id")) 
	items = db.relationship("BucketlistItem", backref=db.backref("bucketlist"))
	users = db.relationship("Users", backref=db.backref("users", lazy="dynamic")) 

	def __repr__(self):
		return "<BucketList: %r>" % self.list_title

class BucketlistItem(db.Model):
	"""
	BucketlistItem
	"""
	__tablename__ = 'items'

	item_id = db.Column(db.Integer, primary_key=True)
	item_title = db.Column(db.String(255))
	item_description = db.Column(db.Text)
	done = db.Column(db.Boolean(), default=False)
	date_created = db.Column(db.DateTime, default=datetime.now)
	date_modified = db.Column(db.DateTime,  onupdate=datetime.now)
	created_by = db.Column(db.Integer, db.ForeignKey("users.user_id"))
	user = db.relationship("Users", backref=db.backref("items", lazy="dynamic"))
	bucketlist_id = db.Column(db.Integer, db.ForeignKey("bucketlist.list_id"))

	def __repr__(self):
		return "<BucketListItem: %r>" % self.item_title




	
		





