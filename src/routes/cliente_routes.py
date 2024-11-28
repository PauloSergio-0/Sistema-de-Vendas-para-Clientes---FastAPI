from fastapi import FastAPI, UploadFile, File, APIRouter
import requests
from domain.datas_processor import DataManipulation
from settings.config import Config
router = APIRouter()

@router.get('/listar/cliente')
def listar_cliente():
    response = requests.get(url= Config().URL_list_produtos)
    
    return response.json()