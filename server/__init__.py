from flask import Flask
from flask_cors import CORS
from server.routes import home, api, portfolio
from server.db import init_db

def create_app(test_config=None):
    app = Flask(__name__, static_url_path='')
    app.config.from_mapping(
        SECRET_KEY='robinhood',
    )

    app.register_blueprint(home)
    app.register_blueprint(portfolio)
    app.register_blueprint(api)

    init_db(app)

    return app