# bachend/app/dependencies.py

from jose             import JWTError, jwt
from fastapi          import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm   import Session

from .         import database
from .database import SessionLocal  

from . import crud, core 
from .models import models

def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(
    token : str = Depends(oauth2_scheme),
    db    : Session = Depends(get_db),) -> models.User:

    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail      = "Não autenticado",
        headers     = {"WWW-Authenticate": "Bearer"},)
    
    try:
        payload = jwt.decode(token, core.SECRET_KEY, algorithms=[core.ALGORITHM])
        user_id: int = int(payload.get("sub"))

    except (JWTError, TypeError, ValueError):
        raise credentials_exception

    user = crud.get_user(db, user_id)
    if not user:
        raise credentials_exception
    
    return user

