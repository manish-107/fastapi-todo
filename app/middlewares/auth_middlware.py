from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from jose import jwt, JWTError

SECRET_KEY = "secret-key"
ALGORITHM = "HS256"

class TokenValidatorMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith(("/signin", "/signup", "/docs", "/openapi.json", "/redoc", "/static")):
            return await call_next(request)


        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(status_code=401, content={"msg": "Authorization header missing or invalid"})

        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            request.state.user = {
                "email": payload.get("sub"),
                "role": payload.get("role")
            }
        except JWTError:
            return JSONResponse(status_code=401, content={"msg": "Invalid or expired token"})

        return await call_next(request)
