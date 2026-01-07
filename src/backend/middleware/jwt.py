from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
import jwt
import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables
load_dotenv()

BETTER_AUTH_SECRET = os.getenv("BETTER_AUTH_SECRET")
if not BETTER_AUTH_SECRET:
    raise ValueError("BETTER_AUTH_SECRET environment variable is required")

async def jwt_middleware(request: Request, call_next):
    # Skip authentication for health check, root, and FastAPI docs endpoints
    if request.url.path in ["/", "/health", "/docs", "/redoc"] or request.url.path.startswith("/openapi.json"):
        response = await call_next(request)
        return response

    # Skip authentication for auth endpoints
    if request.url.path.startswith("/api/auth/"):
        response = await call_next(request)
        return response

    # Extract token from Authorization header
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return JSONResponse(
            status_code=401,
            content={"detail": "Not authenticated: Missing or invalid Authorization header"}
        )

    token = auth_header[7:]  # Remove "Bearer " prefix

    try:
        # Decode the JWT token
        payload = jwt.decode(token, BETTER_AUTH_SECRET, algorithms=["HS256"])

        # Extract user_id from token (using 'sub' as the user identifier)
        user_id = payload.get("sub")
        if not user_id:
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid token: missing user ID"}
            )

        # Add user_id to request state for use in route handlers
        request.state.user_id = user_id

    except jwt.ExpiredSignatureError:
        return JSONResponse(
            status_code=401,
            content={"detail": "Token has expired"}
        )
    except jwt.InvalidTokenError:
        return JSONResponse(
            status_code=401,
            content={"detail": "Invalid token"}
        )

    response = await call_next(request)
    return response