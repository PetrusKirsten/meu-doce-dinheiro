# backend/app/api/routes/auth.py

from fastapi          import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm   import Session

from backend.app.schemas.schemas import TokenOut
from backend.app.dependencies    import get_db
from backend.app.crud.crud       import authenticate_user
from backend.app.core.security   import create_access_token

router = APIRouter(tags=["auth"])

@router.post("/auth/login", response_model=TokenOut, summary="Login via OAuth2 Password")

def login(
    form_data : OAuth2PasswordRequestForm = Depends(),
    db        : Session = Depends(get_db)):

    user = authenticate_user(db, form_data.username, form_data.password)
    
    if not user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
                            detail      = "Credenciais inválidas",
                            headers     = {"WWW-Authenticate": "Bearer"})
    
    access_token = create_access_token({"sub": str(user.id)})
    
    return {"access_token": access_token, "token_type": "bearer"}
