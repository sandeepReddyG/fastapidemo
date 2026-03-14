from fastapi import APIRouter, HTTPException, Depends
from app.models.users import User
from sqlalchemy.orm import Session
from app.models.schemas import UserCreateSchema, UserUpdateSchema, UserResponseSchema,UserSchema
from app.services.user_service import create_user, get_user, update_user, delete_user ,get_all_users

from app.core.database import SessionLocal

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserResponseSchema)
async def create_new_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    """
    Endpoint to create a new user.

    Args:
        user (UserCreate): The user creation request model.
        db (Session): The database session.

    Returns:
        UserResponse: The created user response model.
    """
    return create_user(db=db, username=user.username, email=user.email)

@router.get("/{user_id}", response_model=UserResponseSchema)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to retrieve a user by ID.

    Args:
        user_id (int): The ID of the user to retrieve.
        db (Session): The database session.

    Returns:
        UserResponseSchema: The retrieved user response model.
    """
    user = get_user(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserResponseSchema)
async def update_existing_user(user_id: int, user: UserUpdateSchema, db: Session = Depends(get_db)):
    """
    Endpoint to update an existing user.

    Args:
        user_id (int): The ID of the user to update.
        user (UserUpdateSchema): The user update request model.
        db (Session): The database session.

    Returns:
        UserResponseSchema: The updated user response model.
    """
    updated_user = update_user(db=db, user_id=user_id, username=user.username)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}", status_code=204)
async def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    """
    Endpoint to delete a user by ID.

    Args:
        user_id (int): The ID of the user to delete.
        db (Session): The database session.
    Returns:
        None
    """
    user = get_user(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    delete_user(db=db, user_id=user_id)

    return None

@router.get("/", response_model=list[UserResponseSchema])
def get_users(db: Session = Depends(get_db)):
    """
    Retrieve all users from the database.

    Args:
        db (Session): The database session.
    Returns:
        list[User]: A list of all user objects.
    """
    return get_all_users(db)
