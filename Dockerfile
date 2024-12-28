# imagem base python 3.10
FROM python:3.10-slim

# pasta de trabalho no conteiner
WORKDIR /app

# envia as dependencias primeiro
COPY requirements.txt /app

# baixar as depêndencias
RUN pip install --no-cache-dir -r requirements.txt 

# envia todos us arquivos para area de trabalho
COPY . /app

# porta de execucao
EXPOSE 8000

# inicia a api
CMD [ "python", "src/app.py" ]