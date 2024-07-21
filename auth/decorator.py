# -*- coding: utf-8 -*-
from functools import wraps
from typing import List
from fastapi import Request, HTTPException, status

from sqlalchemy.orm import Session

from auth.middleware import get_current_user
from main_app.database import SessionLocal
from user.repository.user.user import get_user_by_parameter


def verify_user_access(expected_access, username):
    db: Session = SessionLocal()
    try:
        db_user = get_user_by_parameter("username", username, db)
        roles = db_user.roles
        for role in roles:
            if role.name in expected_access:
                return True

        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")
    except:
        raise
    finally:
        db.close()


def has_roles(required_roles: List[str]):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            request: Request = kwargs.get("request")
            username = get_current_user(request=request)
            if not verify_user_access(required_roles, username):
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")

            # Call the original function
            return func(*args, **kwargs)

        return wrapper

    return decorator
