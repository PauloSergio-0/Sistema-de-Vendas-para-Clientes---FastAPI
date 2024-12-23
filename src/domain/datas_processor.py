import pandas as p
import io
from service.api_flask import Api_Flask
from fastapi import UploadFile, HTTPException, status, requests

class DataManipulation:
    def __init__(self):
        self.api_Flask = Api_Flask
        
        
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

                for index, item in cliente.iterrows():
                    json_Cliente = {
                        "id": item['ID'],
                        "nome": item['Nome'],
                        "endereco": item["Endereço"],
                        "contato": item['Contato']
                    }

                    self.api_Flask.send_datas("Cliente", json_Cliente)

                return {"mensagem": f"Upload do Arquivo {File.filename} feita com sucesso!!"}
            except Exception as e:
                raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail= f"Erro ao maniplular csv: {str(e)} ")

        else:
            raise HTTPException(status_code= status.HTTP_406_NOT_ACCEPTABLE,detail= f"Erro o arquivo deve ser no formato .csv: {str(e)} ")

    async def Upload_Produtos(self, File: UploadFile):
        if File.filename.endswith(".csv"):
            try:
                data = await File.read()
                data_decode = io.StringIO(data.decode('utf-8'))
                produto = p.read_csv(data_decode, sep = ',')

                colunas_Produtos = ['ID', 'Nome', 'Código', 'Categoria', 'Preço']
                for coluna in produto.columns:
                    if coluna not in colunas_Produtos:
                        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= f"""Erro: Coluna '{str(coluna)}' não aceita pelo sistema. Verificar a integridade do arquivo {File.filename}""")

                for index, item in produto.iterrows():

                    json_produto = {
                                    "id": item['ID'],
                                    "nome": item['Nome'],
                                    "codigo": item['Código'],
                                    "categoria":item['Categoria'],
                                    "preco": item["Preço"]
                                    }
                    self.api_Flask.send_datas('Produto', json_produto)

                return {"mensagem": f"upload de {File.filename} feito com sucesso!!"}
            except Exception as e:
                raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= f"erro ao manipular csv {str(e)}")

        else:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f"O arquivo deve ser formato .'csv")

    async def upload_vendas(self, File: UploadFile):

        if File.filename.endswith('.csv'):
            try:
                data = await File.read()
                data_decode = io.StringIO(data.decode('utf-8'))
                vendas = p.read_csv(data_decode, sep= ',')
                
                colunas_vendas = ['ID do Cliente', 'ID do Produto', 'Quantidade', 'Data da Venda']

                for coluna in vendas.columns:
                    if coluna not in colunas_vendas:
                        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= f"""Erro: Coluna '{str(coluna)}' não aceita pelo sistema. Verificar a integridade do arquivo {File.filename}""")

                for index, item in vendas.iterrows():
                    json_venda = {
                        "id_cliente": item['ID do Cliente'],
                        "id_produto": item['ID do Produto'],
                        "qtd": item['Quantidade'],
                        "data": item['Data da Venda']
                    }
                    self.api_Flask.send_datas('Venda', json_venda)

            except Exception as e:
                raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= f"erro ao manipular csv {str(e)}") 