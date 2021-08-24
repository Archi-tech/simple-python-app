from flask import Blueprint

api = Blueprint('health_check', __name__)

@api.route('/health_check')
def health_check():
    return 'OK'
