from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key")


def authorized(api_key: str = Depends(api_key_header)) -> None:
    if api_key != "password":
        raise HTTPException(status_code=401, detail="Invalid API key")
