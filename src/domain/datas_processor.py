import pandas as p
from fastapi import UploadFile, HTTPException, status, requests
import io

class DataManipulation:
    def __init__(self):
        self.api_Flask = None
        
        
    async def upload_Cliente(self, File: UploadFile):
        
        if File.filename.endswith(".csv"):
            try:
                data = await File.read()
                data_decode = io.StringIO(data.decode('utf-8'))
                cliente =  p.read_csv(data_decode, sep=',')
                
                
                colunas_clientes = ['ID', 'Nome', 'Endereço', 'Contato']
                
                
                for column in cliente.columns:
                    
                    if column not in colunas_clientes:
                        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail= f"""Erro: Coluna '{str(column)}' não aceita pelo sistema. Verificar a integridade do arquivo {File.filename}""")
                
            except Exception as e:
                raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail= f"Erro o deve ser no .csv: {str(e)} ")
            
            #Success 
            return {"mensagem": f"Upload do Arquivo {File.filename} feita com sucesso!!"}
        else:
            raise HTTPException(status_code= status.HTTP_406_NOT_ACCEPTABLE,detail= f"Erro o arquivo deve ser no formato .csv: {str(e)} ")