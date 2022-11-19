from flask import Blueprint, render_template, session, redirect
from server.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
  return '<p>Home</p>'