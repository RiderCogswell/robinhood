from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g # global variable

load_dotenv() # make use of the .env file

# Create a connection to the database
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base() # stores classes and tables

def init_db():
    Base.metadata.create_all(engine)

    app.teardown_appcontext(close_db)

def get_db():
    if 'db' not in g:
        g.db = Session() # store the database connection in the global variable

    return g.db

def close_db(e=None):
    db = g.pop('db', None) # looks for the db in the global variable, and removes it

    if db is not None:
        db.close()