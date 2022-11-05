# from .crud_device import device
from .crud_device import device
from .crud_device_model import deviceModel
from .crud_user import user
from .crud_users_owner import usersOwner
from .crud_users_subscriptions import usersSubscriptions

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
