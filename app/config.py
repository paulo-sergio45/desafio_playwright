import os

from dotenv import load_dotenv

load_dotenv()

pg_user: str = os.getenv("SQL_USER")
pg_pass: str = os.getenv("POSTGRES_PASSWORD")
pg_host: str = os.getenv("SQL_HOST")
pg_database: str = os.getenv("SQL_DB")

jwt_secret_key: str = os.getenv("SECRET_KEY")
jwt_algorithm: str = os.getenv("ALGORITHM")
jwt_access_toke_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

ASYNCPG_URL: str = f"postgresql+asyncpg://{pg_user}:{pg_pass}@{pg_host}:5432/{pg_database}"

URL_SCRAPER: str = os.getenv("URL_SCRAPER")
