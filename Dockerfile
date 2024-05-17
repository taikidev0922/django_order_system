# ベースイメージとしてPython 3.9を使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# システムの依存関係をインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    git

# Pythonの依存関係をインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクトのソースコードをコピー
COPY . /app

# コンテナが起動したときに実行するコマンド
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django_order_system.wsgi:application"]
