from flask import Blueprint, render_template, session, redirect
from server.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/login')
def login():
  if session.get('logged_in') is None:
    return redirect('/')
