from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo  # Untuk Python 3.9+
from models import Token, UserInDB, hardcoded_users

# Konfigurasi JWT
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Router untuk autentikasi
router = APIRouter()

# Fungsi untuk membuat token JWT
def create_access_token(data: dict):
    # expire = datetime.now(ZoneInfo("UTC")) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = data.copy()
    # to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Endpoint login (/token)
@router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Validasi user berdasarkan username dan password
    # print(f"Login attempt: {form_data.username}, {form_data.password}")  # Tambahkan log
    user = hardcoded_users.get(form_data.username)
    if not user or user.password != form_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    
    # Buat token JWT
    access_token = create_access_token(
        data={"username": form_data.username, "user_id": user.user_id}
    )
    return {
        "access_token": access_token, 
        "token_type": "bearer",
        "username": form_data.username,  # Tambahkan username
        "user_id": user.user_id,        # Tambahkan user_id
        }

