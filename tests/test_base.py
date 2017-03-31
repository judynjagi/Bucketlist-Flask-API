from flask_testing import TestCase

from bucketlist import app, db
from bucketlist.resources.models import Users


class BaseTestCase(TestCase):
	"""A base test case for tests."""
	default_username = 'judy'
	default_password = 'kingslayer'
	default_email = 'judy@example.com'

	def create_app(self):
		app.config.from_object('configsettings.config.TestingConfig')
		return app

	def setUp(self):
		db.create_all()
		user = Users(username=self.default_username, password=self.default_password,
                 verify_password=self.default_password, email=self.default_email)
		db.session.add(user)
		db.session.commit()


	def tearDown(self):
		db.session.remove()
		db.drop_all()