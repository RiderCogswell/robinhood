from datetime import datetime
from server.db import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Purchase(Base):
  __tablename__ = 'purchases'
  id = Column(Integer, primary_key=True)
  title = Column(String(50), nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
  description = Column(String(100), nullable=False)
  price = Column(Integer, nullable=False)
  created_at = Column(DateTime, default=datetime.now)

  user = relationship('User', back_populates='purchases')