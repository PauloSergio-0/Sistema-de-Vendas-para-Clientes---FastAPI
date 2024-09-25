import pandas as pd
import sqlite3 as con
import os
from io import StringIO
from fastapi import UploadFile, HTTPException, status 



class Database_manipulation:
    def __init__(self):
        self.connection = con.connect('src/data/vendas_clientes.db')
        self.cursor = self.connection.cursor()
        
    
    def close_db(self):
        try:
            self.connection.close()
            
        except con.DatabaseError as error:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail = f"Error closing database error: {error}")
            
    def create_colluns_db(self):
        
        sql_cliente = """
        CREATE TABLE IF NOT EXISTS Cliente (
            ID_cliente INTEGER PRIMARY KEY NOT NULL,
            Nome_cliente VARCHAR(80) NOT NULL,
            Endereco_cliente VARCHAR(80) NOT NULL,
            Contato_cliente VARCHAR(80) NOT NULL
        )
        """
        
        sql_produtos = """
        CREATE TABLE IF NOT EXISTS Produtos (
            ID_produto INTEGER PRIMARY KEY NOT NULL,
            Nome_produto VARCHAR(80) NOT NULL,
            Codigo_produto INTEGER NOT NULL,
            Categoria_produto VARCHAR(40) NOT NULL,
            Preco_produto FLOAT NOT NULL
        )
        """
        
        sql_vendas = """
        CREATE TABLE IF NOT EXISTS Vendas (
            ID_Cliente INTEGER NOT NULL, 
            ID_produto INTEGER NOT NULL,
            Qtde_venda INTEGER NOT NULL,
            Data_venda DATETIME NOT NULL,
            FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_cliente),
            FOREIGN KEY (ID_produto) REFERENCES Produtos(ID_produto)
        )
        """
        
        try:
            self.cursor.execute(sql_cliente)
            
            self.cursor.execute(sql_produtos)
            
            self.cursor.execute(sql_vendas)
            
            self.connection.commit()
            
            
            return True
        
        except con.DatabaseError as error:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail=f"Error create tables in database error: {error}")
        
        
        
        
    async def insert_data_cliente(self, File: UploadFile):
        
        sql_insert_client = """
        INSERT INTO Cliente (ID_cliente, Nome_cliente, Endereco_cliente, Contato_cliente)
        VALUES (?, ?, ?, ?)
        """
        
        if self.create_colluns_db() and File.filename.endswith(".csv"):
            
            
            data_cliente = []
            
            data_file = await File.read()
            
            df_cliente = pd.read_csv(StringIO(data_file.decode('utf-8')),
                                    sep=',',
                                    dtype = {
                                        "ID": "string",
                                        "Nome": "string",
                                        "Endereço": "string",
                                        "Contato": "string"
                                    })
            
            for index, row in df_cliente.iterrows():
                content = (row.iloc[0], row.iloc[1], row.iloc[2], row.iloc[3])
                data_cliente.append(content)
                
            try:
                for line_cliente in data_cliente:
                    self.cursor.execute(sql_insert_client, line_cliente)
                
                self.connection.commit()
                self.close_db()
                return {"menssage": "Dados inseridos com sucesso"}
            except con.DatabaseError as e:
                raise HTTPException(status.HTTP_400_BAD_REQUEST, 
                            detail=f"Erro ao inserir dados: {e}")
        else:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, 
                            detail="Erro de fluxo")

