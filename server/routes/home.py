from flask import Blueprint, render_template, session, redirect
from server.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/')
def index():
  if session.get('loggedIn') == True:
    return render_template('home/index.html')
  return redirect('/login')

@bp.route('/login')
def login():
  if session.get('logged_in') is None:
    return redirect('/')
