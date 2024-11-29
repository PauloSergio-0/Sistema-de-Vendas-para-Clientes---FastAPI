from fastapi import UploadFile, File, APIRouter
import requests
from domain.datas_processor import DataManipulation
from settings.config import Config

router = APIRouter()


@router.post("/importar-produtos/")
async def produto_file(file: UploadFile = File(...)):
    return await DataManipulation().Upload_Produtos(file)

@router.get("/listar/produtos")
def lista_clientes():
    response = requests.get(url=Config.URL_list_produto)
    return response.json()