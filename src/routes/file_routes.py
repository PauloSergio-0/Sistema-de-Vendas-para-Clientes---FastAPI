from fastapi import FastAPI, UploadFile, File, APIRouter
from domain.Files_processor import Database_manipulation

router = APIRouter()


@router.post("/importar-clientes/")
async def cliente_file(file: UploadFile = File(...)):
    return await Database_manipulation().insert_data_cliente(file)
    
    

# @router.post("/importar-produtos/")

# @router.post("/importar-vendas/")
