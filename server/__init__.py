from flask import Flask
from flask_cors import CORS
from server.routes import home, api, portfolio
from server.db import init_db

def create_app(test_config=None):
    app = Flask(__name__, static_url_path='')
    CORS(app, supports_credentials=True)
    app.config.from_mapping(
        SECRET_KEY='robinhood',
    )

    @app.route('/quote')
    def quote():
      try:
            symbol = request.args.get('symbol', None)

            quote = yf.Ticker(symbol)

            return jsonify(quote.info)
      except:
            print(sys.exc_info()[0])

            return jsonify(message = 'Could not get quote'), 500

    app.register_blueprint(home)
    app.register_blueprint(portfolio)
    app.register_blueprint(api)

    init_db(app)

    return app
