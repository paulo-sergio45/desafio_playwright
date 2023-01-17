from asyncio import current_task
from typing import AsyncGenerator

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_scoped_session
from sqlalchemy.orm import sessionmaker, declarative_base

from app import config

url = config.ASYNCPG_URL

Base = declarative_base()

engine = create_async_engine(
    url,
    future=True,
    echo=True,
    json_serializer=jsonable_encoder,
)

async_session_factory = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
AsyncScopedSession = async_scoped_session(async_session_factory, scopefunc=current_task)


async def get_db() -> AsyncGenerator:
    async with async_session_factory() as session:
        try:
            yield session
            await session.commit()
        except SQLAlchemyError as sql_ex:
            await session.rollback()
            raise sql_ex
        except HTTPException as http_ex:
            await session.rollback()
            raise http_ex
        finally:
            await session.close()
