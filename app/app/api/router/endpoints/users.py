from typing import Any

import app.crud as crud
import app.models as models
import app.schemas as schemas
from app.api import deps
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=schemas.User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
    current_user: models.User = Depends(deps.get_current_active_adminuser),
) -> Any:
    """
    Create new user.
    """
    user = crud.db.user.get_by_username(db, username=user_in.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )

    if user_in.email:
        user = crud.db.user.get_by_email(db, email=user_in.email)
        if user:
            raise HTTPException(
                status_code=400,
                detail="The user with this email already exists in the system.",
            )

    user = crud.db.user.create(db, obj_in=user_in, owner_id=current_user.id)

    return user


@router.put("/me", response_model=schemas.User)
def update_user_me(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(None),
    username: str = Body(None),
    email: EmailStr = Body(None),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update own user.
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = schemas.UserUpdate(**current_user_data)

    if password is not None:
        user_in.password = password

    if username is not None:
        user_in.username = username

        user = crud.db.user.get_by_username(db, username=user_in.username)
        if user:
            raise HTTPException(
                status_code=400,
                detail="The user with this username already exists in the system.",
            )

    if email is not None:
        user_in.email = email

        if user_in.email:
            user = crud.db.user.get_by_email(db, email=user_in.email)
            if user:
                raise HTTPException(
                    status_code=400,
                    detail="The user with this email already exists in the system.",
                )

    user = crud.db.user.update(db, db_obj=current_user, obj_in=user_in)
    return user


@router.put("/{user_id}", response_model=schemas.User)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    user_in: schemas.UserUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a user.
    """
    user = crud.db.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )

    # user_in.is_adminuser = user.is_adminuser

    # if user == current_user or crud.db.user.is_adminuser(current_user):
    #     user = crud.db.user.update(db, db_obj=user, obj_in=user_in)
    #     return user
    # else:
    #     raise HTTPException(
    #         status_code=400, detail="The user doesn't have enough privileges"
    #     )
