from fastapi import UploadFile, File, APIRouter, HTTPException, status
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

@router.get("/filter/produto")
def filter_produto(id_produto: int):
    parametros = {"id_produto": id_produto}
    
    response = requests.get(url = Config.URL_filter_produto, params = parametros)    
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= response.json()) 
    
    
@router.put("/delete/produto")
def deletar_produto(id_produto: int):
    parametros = {"id_produto": id_produto}
    
    response = requests.patch(url = Config.URL_delete_produto, params = parametros)    
    if response.status_code == 201:
        return response.json()
    else:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= response.json())
    
@router.put("/desactivate/produto")
def deletar_produto(id_produto: int):
    parametros = {"id_produto": id_produto}
    
    response = requests.put(url = Config.URL_desavtivate_produto, params = parametros)    
    if response.status_code == 201:
        return response.json()
    else:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= response.json())
    