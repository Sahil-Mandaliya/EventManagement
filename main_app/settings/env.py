from os import environ
import json
from alembic import context
from sqlalchemy import engine_from_config, pool

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = environ.get("DATABASE_URL")