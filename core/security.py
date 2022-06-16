from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(password_plain: str, password_encode: str) -> bool:
    return pwd_context.verify(password_plain, password_encode)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
