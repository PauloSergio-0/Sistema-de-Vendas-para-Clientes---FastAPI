from fastapi import UploadFile, File, APIRouter
import requests
from domain.datas_processor import DataManipulation
from settings.config import Config

router = APIRouter()

@router.post("/importar-vendas/")
async def venda_file(file: UploadFile = File(...)):
    return await DataManipulation().upload_vendas(file)

@router.get("/listar/vendas")
def lista_clientes():
    response = requests.get(url=Config.URL_list_venda)
    return response.json()

