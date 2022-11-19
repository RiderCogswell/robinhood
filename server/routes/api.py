from flask import Blueprint, jsonify, request, session
from server.models import User, Purchase
from server.db import get_db
from server.utils.stocks import get_company_info
from server.utils.auth import login_required
import sys

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def create_user():
  data = request.get_json()
  db = get_db()

  try: 
    newUser = User(
      username=data['username'],
      email=data['email'],
      password=data['password']
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
  return jsonify(id = newUser.id)

@bp.route('/users/login', methods=['POST'])
def login():
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

@bp.route('/users/logout', methods=['POST'])
def logout():
  # remove session variables
  session.clear()
  return '', 204

@bp.route('/purchases', methods=['POST'])
@login_required
def purchase():
  data = request.get_json()
  db = get_db()

  try:
    company = get_company_info(data['symbol'])

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