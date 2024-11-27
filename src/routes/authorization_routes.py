from fastapi import HTTPException, APIRouter
from service.auth_service import Authorization_service
from settings.config import Config
import requests

router = APIRouter()

@router.get("/send-to-flask")
def send_to_flask():
    
    # token_data = {"sub": "FastAPI"}
    
    # access_token = Authorization_service.create_access_token(token_data)

    url = Config.URL_AUTHORIZATION
    
    # headers = {"Authorization": f"Bearer {access_token}"}
    headers = Authorization_service.create_access_token()
    
    response = requests.get(url, headers=headers)
    
    
    
    if response.status_code != 200:
        raise HTTPException(response.status_code, detail=response.json())
    
    return response.json()