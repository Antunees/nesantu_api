import json
import logging
from typing import Any, Dict, List, Optional, Union

import app.crud as crud
from app.broker.broker_db import Broker
from app.core.security import get_password_hash, verify_password
from app.crud.db.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from sqlalchemy.orm import Session


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_id(self, db: Session, *, id: int) -> Optional[User]:
        return db.query(User).filter(User.id == id).first()

    def get_by_username(self, db: Session, *, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()

    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def get_by_id(self, db: Session, *, id: int) -> Optional[User]:
        return db.query(User).filter(User.id == id).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            username=obj_in.username,
        )

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        crud.broker.user.set(db_obj)

        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data.get("password"):
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password

        user = super().update(db, db_obj=db_obj, obj_in=update_data)

        if user:
            crud.broker.user.set(user)

        return user

    def authenticate(self, db: Session, *, username: str, password: str) -> Optional[User]:
        if user := self.get_by_username(db, username=username):
            return user if verify_password(password, user.hashed_password) else None
        else:
            return None

    def is_active(self, user: User) -> bool:
        return user.is_active


user = CRUDUser(User)
