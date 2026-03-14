from sqlalchemy.orm import Session
from app.models.users import User

def create_user(db: Session, username: str, email: str) -> User:
    """
    Create a new user in the database.

    Args:
        db (Session): The database session.
        username (str): The username of the new user.
        email (str): The email of the new user.

    Returns:
        User: The created user object.
    """
    new_user = User(username=username, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user(db: Session, user_id: int, username: str = None) -> User:
    """
    Update an existing user in the database.
    Args:
        db (Session): The database session.
        user_id (int): The ID of the user to update.
        username (str, optional): The new username of the user.
        email (str, optional): The new email of the user.
    Returns:
        User: The updated user object.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        if username:
            user.username = username
        db.commit()
        db.refresh(user)
    return user

def delete_user(db: Session, user_id: int) -> None:
    """
    Delete a user from the database.

    Args:
        db (Session): The database session.
        user_id (int): The ID of the user to delete.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()

def get_user(db: Session, user_id: int) -> User:
    """
    Retrieve a user by ID from the database.

    Args:
        db (Session): The database session.
        user_id (int): The ID of the user to retrieve.

    Returns:
        User: The user object if found, else None.
    """
    return db.query(User).filter(User.id == user_id).first()

def get_all_users(db: Session) -> list[User]:
    """
    Retrieve all users from the database.

    Args:
        db (Session): The database session.
    Returns:
        list[User]: A list of all user objects.
    """
    return db.query(User).all()