from typing import TYPE_CHECKING

from app.db.base_class import Base
from sqlalchemy import Boolean, ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship

# if TYPE_CHECKING:
    # from .example import Example  # noqa: F401


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_email_valited = Column(Boolean(), default=True)
    examples = relationship("Example", back_populates="example")
