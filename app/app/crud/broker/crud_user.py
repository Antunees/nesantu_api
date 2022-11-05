
import json
import logging
from app.models.user import User
from app.broker.broker_db import Broker
from typing import List, Optional


class CRUDUser():
    def set(self, user: User) -> None:
        Broker.DB0.set(f'user:{user.id}', json.dumps(user.as_dict()))

    def get(self, id: int) -> Optional[User]:
        try:
            user_broker = json.loads(Broker.DB0.get(f'user:{id}'))
            return User(**user_broker)
        except Exception as e:
            logging.warning('CRUDUser get e')
            logging.warning(e)
            return None

    def is_active(self, user: User) -> Optional[User]:
        try:
            return user.is_active
        except Exception as e:
            logging.warning('CRUDUser is_active e')
            logging.warning(e)
            return None


user = CRUDUser()
