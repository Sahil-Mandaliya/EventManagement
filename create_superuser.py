# -*- coding: utf-8 -*-
import argparse
from user.models.user import Role, User
from main_app.utils.utils import hash_password

from main_app.database import SessionLocal


def create_superuser(username: str, password: str, email: str, full_name: str, phone: str):
    db = SessionLocal()
    hashed_password = hash_password(password)
    superuser = User(
        username=username,
        email=email,
        full_name=full_name,
        phone=phone,
        hashed_password=hashed_password,
    )

    role_names = ["admin", "user"]
    roles = []
    for role_name in role_names:
        role = db.query(Role).filter(Role.name == role_name).first()
        if not role:
            db_role = Role(name=role_name)
            roles.append(db_role)
            db.add(db_role)

    superuser.roles = roles
    db.add(superuser)
    db.commit()

    return superuser


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a superuser for FastAPI")
    parser.add_argument("--username", required=True, help="Superuser's username")
    parser.add_argument("--password", required=True, help="Superuser's password")
    parser.add_argument("--email", required=True, help="Superuser's email")
    parser.add_argument("--full_name", required=True, help="Superuser's full name")
    parser.add_argument("--phone", required=True, help="Superuser's phone number")

    args = parser.parse_args()
    create_superuser(args.username, args.password, args.email, args.full_name, args.phone)
