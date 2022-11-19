from flask import Blueprint, render_template, session
from server.db import get_db
from server.models import Purchase
from server.utils.auth import login_required

bp = Blueprint('portfolio', __name__, url_prefix='/portfolio')

@bp.route('/')
@login_required
def portfolio():
  db = get_db()
  purchases = (
    db.query(Purchase)
    .filter(Purchase.user_id == session.get('user_id'))
    .all()
  )

  return render_template(
    'portfolio/index.html', 
    purchases=purchases,
    loggedIn=session.get('loggedIn')
  )

@bp.route('/sell/<id>')
@login_required
def sell(id):
  db = get_db()
  purchase = (
    db.query(Purchase)
    .filter(Purchase.id == id)
    .one()
  )

  return render_template(
    'portfolio/sell.html', 
    purchase=purchase,
    loggedIn=session.get('loggedIn')
  )