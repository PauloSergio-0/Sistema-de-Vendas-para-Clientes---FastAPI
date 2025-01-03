from fastapi import FastAPI, UploadFile, File, APIRouter, HTTPException, status
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

@router.get('/filter/cliente')
def filtro_cliente(id_cliente: int):
    paramentros = {'id_cliente':id_cliente}
    response = requests.get(url= Config.URL_filter_cliente, params = paramentros)
    return response.json()

@router.patch('/delete/cliente')
def deletar_cliente(id_cliente: int):
    paramentros = {'id_cliente':id_cliente}
    response = requests.patch(url= Config.URL_delete_cliente, params = paramentros)
    if response.status_code == 201:
        return response.json()
    else:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= response.json())

@router.put('/desactivate/cliente')
def desativar_cliente(id_cliente: int):
    paramentros = {'id_cliente':id_cliente}
    response = requests.put(url= Config.URL_desactivate_cliente, params = paramentros)
    
    if response.status_code == 201:
        return response.json()
    else:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= response.json())