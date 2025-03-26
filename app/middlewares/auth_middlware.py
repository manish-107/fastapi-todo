from fastapi import Request, HTTPException
from app.services.auth_service import verify_access_token

async def auth_middleware(request: Request):
    token = request.headers.get("Authorization")
    
    if not token or not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized access")
    
    token = token.split("Bearer ")[1]

    payload = verify_access_token(token)

    return payload  
