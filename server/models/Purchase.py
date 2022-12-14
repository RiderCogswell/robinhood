from datetime import datetime
from server.db import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Purchase(Base):
  __tablename__ = 'purchases'
  id = Column(Integer, primary_key=True)
  symbol = Column(String(50), nullable=False)
  shares = Column(Integer, nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
  price = Column(Integer, nullable=False)
  purchased_at = Column(DateTime, default=datetime.now)

  user = relationship('User')