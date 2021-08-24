from flask import Flask
from blueprint.health_check import api as health_check_api
from blueprint.post import api as post_api

app = Flask(__name__)

app.register_blueprint(health_check_api)
app.register_blueprint(post_api)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
