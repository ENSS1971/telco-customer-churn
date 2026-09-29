# 1. Imagem base oficial do Python
FROM python:3.10-slim

# 2. Variáveis de ambiente para evitar arquivos .pyc e garantir logs em tempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# 4. Instala dependências de sistema mínimas necessárias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    make \
    && rm -rf /var/lib/apt/lists/*

# 5. Copia o arquivo de dependências e instala os pacotes Python + JupyterLab
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir jupyterlab

# 6. Copia todos os arquivos do projeto para dentro do contêiner
COPY . .

# 7. Expõe as portas para o JupyterLab (8888) e Streamlit (8501)
EXPOSE 8888 8501

# 8. Comando padrão ao iniciar o contêiner: abrir o JupyterLab livre de senha para desenvolvimento local
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]