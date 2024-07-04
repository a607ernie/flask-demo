# 使用官方的Python映像作為基礎映像
FROM python:3.9-slim

# 設置工作目錄
WORKDIR /app

# 複製當前目錄的內容到工作目錄
COPY ./app/requirements.txt /app/


# 安裝必要的Python包
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest

# 复制应用程序到工作目录
COPY . /apps

# 暴露應用運行的端口
EXPOSE 5001

# Define environment variable
ENV FLASK_APP=app.py

# 定義運行命令
CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:5001", "wsgi:app"]
