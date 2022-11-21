from os import getenv
from flask import Flask, Blueprint, jsonify, request, session
from flask_cors import cross_origin
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, jwt_required, JWTManager, unset_jwt_cookies
from server.models import User, Purchase
from server.db import get_db
from server.utils.stocks import Stock
import yfinance as yf
import sys


bp = Blueprint('api', __name__, url_prefix='/api')

# bp.config["JWT_SECRET_KEY"] = getenv("JWT_SECRET_KEY")
# jwt = JWTManager()

@bp.route('/data', methods=['GET'])
@cross_origin(supports_credentials=True)
def data(ticker):
  info = map(ticker)
  return info

@bp.route('/user', methods=['POST'])
def signup():
  data = request.get_json()
  db = get_db()

  try: 
    newUser = User(
      username = data['username'],
      email = data['email'],
      password = data['password']
    )

    db.add(newUser)
    db.commit()
  except:
    print(sys.exc_info()[0]) # send error

    db.rollback() # rollback commit

    return jsonify(message = 'Signup failed'), 500

  session.clear()
  session['user_id'] = newUser.id
  session['loggedIn'] = True
  return jsonify(
    id = newUser.id,
    username = newUser.username,
    email = newUser.email,
    password = newUser.password
    ), 200

@bp.route('/users', methods=['GET'])
def get_all_users():
  try:
    db = get_db()
    print(db)
    users = db.query(User).all()
    return jsonify(users)
  except:
    print(sys.exc_info()[0])
    print(db)
    return jsonify(message = 'Could not get users'), 500

@bp.route('/login', methods=['POST'])
def login():
  # email = request.json.get('email', None)
  # password = request.json.get('password', None)
  # if email != '' or password != '':
  #   return jsonify({"msg": "Bad email or password"}), 401

  # access_token = create_access_token(identity=email)
  # response = {"access_token": access_token}
  # return jsonify(response), 200
  data = request.get_json()
  db = get_db()

  try:
    user = db.query(User).filter(User.email == data['email']).one()
  except:
    print(sys.exc_info()[0])

    if user.verify_pw(data['password']) == False: # data['password'] is used as the pw argument in verify_pw func because self has already reserved the first spot
      return jsonify(message = 'Incorrect credentials'), 400

  session.clear()
  session['user-id'] = user.id
  session['loggedIn'] = True

  return jsonify(id = user.id)

@bp.route('/logout', methods=['POST'])
def logout():
  # remove session variables
  session.clear()
  return '', 204

@bp.route('/purchases/<symbol>', methods=['POST'])
def purchase(symbol):
  data = request.get_json()
  db = get_db()

  try:

    company = Stock(symbol).get_company_info(symbol)
    newPurchase = Purchase(
      user_id=session.get('user_id'),
      symbol=data['symbol'],
      shares=data['shares'],
      price=company['price']
    )

    db.add(newPurchase)
    db.commit()
  except:
    print(sys.exc_info()[0])

    db.rollback()

    return jsonify(message = 'Purchase failed'), 500

  return jsonify(id = newPurchase.id)

@bp.route('/quote', methods=['GET'])
def get_quote():
  try:
    symbol = request.args.get('symbol', None)

    quote = yf.Ticker(symbol)

    return jsonify(quote.info)
  except:
    print(sys.exc_info()[0])

    return jsonify(message = 'Could not get quote'), 500