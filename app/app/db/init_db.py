
import app.crud as crud
import app.schemas as schemas
from sqlalchemy.orm import Session

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)


    user = crud.db.user.get_by_username(db, username="apple")
    if not user:
        user_in = schemas.UserCreate(
            username="cap",
            password="cap",
        )
        user = crud.db.user.create(db, obj_in=user_in, is_adminuser=True)  # noqa: F841
