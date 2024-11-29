from fastapi import FastAPI, UploadFile, File, APIRouter
import requests
from domain.datas_processor import DataManipulation
from settings.config import Config

router = APIRouter()

@router.post("/importar-clientes/")
async def cliente_file(file: UploadFile = File(...)):
    return await DataManipulation().upload_Cliente(file)

@router.get('/listar/cliente')
def listar_cliente():
    response = requests.get(url= Config().URL_list_cliente)
    
    return response.json()