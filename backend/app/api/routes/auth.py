from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from dependencies import get_db
from schemas.auth import LoginIn, TokenOut
from ..crud.user import authenticate_user
from ..core.security import create_access_token

router = APIRouter(tags=["auth"])

@router.post("/auth/login", response_model=TokenOut)
def login(login_in: LoginIn, db: Session = Depends(get_db)):
    user = authenticate_user(db, login_in.email, login_in.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token({"sub": str(user.id)})
    
    return {"access_token": access_token}
