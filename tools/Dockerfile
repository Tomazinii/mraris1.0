
FROM python:3.8-alpine

# Define variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "/code/tools:/code/tools"

# Define o diretório de trabalho
WORKDIR /code

# Copia o arquivo de requisitos
COPY requirements.txt .

# Instala as dependências do apk e do pip
RUN apk update && \
    apk add --no-cache python3-tkinter && \
    rm -rf /var/cache/apk/* && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Copia o código fonte
COPY . .

# Define o diretório de trabalho específico
WORKDIR /code/web/fastapi_app

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


# FROM python:3.8-alpine
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
# WORKDIR /code
# ENV PYTHONPATH "code/tools:/code/tools"
# COPY requirements.txt .
# RUN apt-get update && apt-get install -y \
#     python3-tk \
#     && rm -rf /var/lib/apt/lists/*
# RUN pip install --upgrade pip && pip install -r requirements.txt
# COPY . .
# RUN ls
# WORKDIR /code/tools/web/fastapi_app

# # CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]