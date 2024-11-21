import requests
from settings.config import Config

class Api_Flask:
    
    
    def send_datas(type_data, data):
        
        if type_data == 'Cliente':
            url = Config.URL_Cliente
        elif type_data == 'Produto':
            url = Config.URL_Produtos
        elif type_data == 'Venda':
            url = Config.URL_Vendas
        else:
            raise {"Erro:" f"Tipo de dados especificado de maneira errada: {type_data} não comtenpla nenhuma condicional"}
        
        try:
            reponse = requests.post(url=url, json=data)
            reponse.raise_for_status()
        except requests.exceptions.HTTPError as e:
            
            raise {"error": f"{str(e)}"}
        
        