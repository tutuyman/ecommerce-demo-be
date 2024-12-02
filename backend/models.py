from pydantic import BaseModel

# Model untuk token
class Token(BaseModel):
    access_token: str
    token_type: str
    username: str  # Tambahkan username
    user_id: int    # Tambahkan user_id

# Model untuk user
class UserInDB(BaseModel):
    user_id: int
    username: str
    password: str
    role: str

# Hardcoded users
hardcoded_users = {
    "test@example.com": UserInDB(user_id=1, username="test@example.com", password="123456", role="user"),
    "admin@example.com": UserInDB(user_id=2, username="admin@example.com", password="admin123", role="admin"),
}
