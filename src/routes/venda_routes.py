from fastapi import UploadFile, File, APIRouter, HTTPException, status
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

@router.get("/filter/venda")
def filter_venda(id_venda: int):
    parametros = {"id_venda": id_venda}
    
    response = requests.get(url= Config.URL_filter_venda, params = parametros)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail= response.json())
    
@router.get("/filter/venda-data")
def filter_venda(data_venda: str):
    parametros = {"data_venda": data_venda}
    
    response = requests.get(url= Config.URL_filter_venda_data, params = parametros)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail= response.json())

@router.patch("/delete/venda")
def delete_venda(id_venda: int):
    parametros = {"id_venda": id_venda}
    
    response = requests.patch(url= Config.URL_delete_venda, params = parametros)
    
    if response.status_code == 201:
        return response.json()
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail= response.json())
    
@router.put("/cancel/venda")
def delete_venda(id_venda: int):
    parametros = {"id_venda": id_venda}
    
    response = requests.put(url= Config.URL_cancel_venda, params = parametros)
    
    if response.status_code == 201:
        return response.json()
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail= response.json())
    
    
@router.post("/sale/venda")
def sale_vendas(id_cliente: int, id_produto: int, qtd_venda: int):
    
    json_venda = {"id_cliente": id_cliente, "id_produto": id_produto, "qtd_venda": qtd_venda}
    
    response = requests.post(url = Config.URL_sale_venda_venda, json= json_venda)
    
    if response.status_code == 201:
        return response.json()
    else:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail= response.json())