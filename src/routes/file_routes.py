from fastapi import FastAPI, UploadFile, File, APIRouter
from domain.Files_processor import Database_manipulation

router = APIRouter()


@router.post("/importar-clientes/")
async def cliente_file(file: UploadFile = File(...)):
    return await Database_manipulation().insert_data_cliente(file)

@router.post("/listar-clientes/")
async def list_cliente():
    return Database_manipulation().listing_cliente()

@router.post("/listar-produtos/")
@router.post("/listar-vendas/")


@router.post("/importar-produtos/")
async def produto_file(file: UploadFile = File(...)):
    return await Database_manipulation().insert_data_produtos(file)

@router.post("/importar-vendas/")
async def venda_file(file: UploadFile = File(...)):
    return await Database_manipulation().insert_data_vendas(file)
