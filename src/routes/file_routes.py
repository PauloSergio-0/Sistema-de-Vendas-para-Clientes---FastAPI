from fastapi import FastAPI, UploadFile, File, APIRouter

from domain.datas_processor import DataManipulation

router = APIRouter()


@router.post("/importar-clientes/")
async def cliente_file(file: UploadFile = File(...)):
    return await DataManipulation().upload_Cliente(file)

@router.post("/importar-produtos/")
async def produto_file(file: UploadFile = File(...)):
    return await DataManipulation().Upload_Produtos(file)

@router.post("/importar-vendas/")
async def venda_file(file: UploadFile = File(...)):
    return await DataManipulation().upload_vendas(file)


