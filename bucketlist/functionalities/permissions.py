from flask import g, jsonify
from flask_httpauth import HTTPTokenAuth
from bucketlist.resources.models import Users

auth = HTTPTokenAuth(scheme='Token')
@auth.error_handler
def unauthorized(message=None):
	"""
	return 403 instead of 401 to prevent browsers from displaying the default
	auth dialog
	"""
	if not message:
		message = "Error: You are not authorized to access this resource."
	return jsonify({ "message": message }), 403

@auth.verify_token
def verify_token(token):
    """Validates the token sent by the user """
    user = Users.verify_auth_token(token)
    if not user:
        return False
    g.user = user
    return True
