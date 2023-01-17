from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

import app.models.user as schemas
import app.orm.user as models
from app.security.password import get_password_hash


async def get_user(db: AsyncSession, user_id: int):
    stmt = select(models.User).where(models.User.id == user_id and models.User.is_active == True)
    result = await db.execute(stmt)
    return result.scalars().first()


async def get_user_by_email(db: AsyncSession, email: str):
    stmt = select(models.User).where(models.User.email == email and models.User.is_active == True)
    result = await db.execute(stmt)
    return result.scalars().first()


async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
    stmt = select(models.User).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().fetchall()


async def create_user(db: AsyncSession, user: schemas.UserCreate):
    hashed_password = await get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user
