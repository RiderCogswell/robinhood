from server.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt

salt = bcrypt.gensalt() # generate a salt (random bits to help encrypt the password)

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(100), nullable=False, unique=True)
  password = Column(String(100), nullable=False)

  @validates('email')
  def validate_email(self, key, email):
    assert '@' in email # ensure email is valid (regex breaks in production so I'm not using it)

    return email

  @validates('password')
  def validate_password(self, key, password):
    assert len(password) > 4

    return bcrypt.hashpw(password.encode('utf-8'), salt) # hash pw

  def verify_pw(self, password):
    return bcrypt.checkpw(
      password.encode('utf-8'),
      self.password.encode('utf-8')
    )