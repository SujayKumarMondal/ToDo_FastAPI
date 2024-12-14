import requests
from fastapi import HTTPException
import os

GOOGLE_OAUTH_CLIENT_ID = os.environ.get("client-id")
GOOGLE_OAUTH_CLIENT_SECRET = os.environ.get("client-secret")

async def verify_google_token(token: str):
    url = f'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token={token}'
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Google authentication failed")
    return response.json()
