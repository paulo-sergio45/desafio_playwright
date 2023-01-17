from passlib.hash import pbkdf2_sha256


async def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pbkdf2_sha256.verify(plain_password, hashed_password)


async def get_password_hash(password: str) -> str:
    return pbkdf2_sha256.using(salt_size=32).hash(password)
