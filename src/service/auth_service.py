from fastapi import HTTPException
from datetime import datetime , timedelta
import jwt
import requests
from settings.auth_config import Config_jwt


class Authorization_service:
    
    def create_access_token():
        token = {"sub": "FastAPI"}
        
        to_encode =  token.copy()

        expire = datetime.now() + timedelta(minutes=Config_jwt.ACCESS_TOKEN_EXPIRE_MINUTES)


        to_encode.update({'exp': int(expire.timestamp())})
        
        encoded_jwt = jwt.encode(to_encode, Config_jwt.SECRET_KEY, algorithm = Config_jwt.AUGORITHM)
        
        headers = {"Authorization": f"Bearer {encoded_jwt}"}
        return headers
        
        

