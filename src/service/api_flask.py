import requests
from settings.config import Config
from service.auth_service import Authorization_service
class Api_Flask:
    
    
    def send_datas(type_data: str, data: dict):
        print(data)
        if type_data == 'Cliente':
            url = Config.URL_Cliente
        elif type_data == 'Produto':
            url = Config.URL_Produtos
        elif type_data == 'Venda':
            url = Config.URL_Vendas
        else:
            raise ValueError("Erro:" f"Tipo de dados especificado de maneira errada: {type_data} não comtenpla nenhuma condicional")
        
        try:
            headers = Authorization_service.create_access_token()
            reponse = requests.post(url=url, json=data, headers=headers)
            reponse.raise_for_status()
            return {"detail": reponse.json() }
        except requests.exceptions.HTTPError as e:
            
            raise {"error": f"{str(e)}"}
        
        