
from typing import List, Optional
from fastapi import Request, HTTPException, status

from pydantic import BaseModel

from auth.auth import verify_access_token


class TokenCredentials(BaseModel):
    token: str


class JWTBearer:
    def __init__(self, auto_error: bool = True):
        self.auto_error = auto_error

    def __call__(self, request: Request) -> Optional[TokenCredentials]:
        authorization: str = request.headers.get('Authorization')
        if authorization:
            scheme, token = authorization.split(" ")
            if scheme.lower() == 'bearer':
                if not token:
                    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED ,detail="No token provided")

                return TokenCredentials(token=token)

        if self.auto_error:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED ,detail="No token provided")
        return None
        

def get_current_user(request: Request):
    if not request:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Request object is required")
    
    jwt_bearer = JWTBearer()
    
    # Manually extract and verify the token
    credentials = jwt_bearer(request)
    token = credentials.token if credentials else None
    
    if token:
        payload = verify_access_token(token)
        if not payload:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token or expired token.")
        
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials.")
        
        return username
   
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token or expired token.")
       
