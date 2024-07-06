#!/bin/bash

# 定義目標目錄和 Git 存儲庫 URL
TARGET_DIR="$HOME/Documents/flask-demo"
REPO_URL="https://github.com/a607ernie/flask-demo.git"

# 檢查目標目錄是否存在
if [ ! -d "$TARGET_DIR" ]; then
  # 目標目錄不存在，進行克隆操作
  mkdir -p "$TARGET_DIR"
  git clone "$REPO_URL" "$TARGET_DIR"
else
  # 目標目錄存在，重置並拉取最新提交
  cd "$TARGET_DIR"
  git reset --hard
  git clean -fd
  git pull origin main
fi

echo "Deployment complete."
