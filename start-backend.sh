#!/bin/bash

echo "========================================"
echo "青研智思 - 后端服务启动脚本"
echo "========================================"
echo ""

cd backend

if [ ! -d "venv" ]; then
    echo "[1/3] 创建虚拟环境..."
    python3 -m venv venv
fi

echo "[2/3] 激活虚拟环境..."
source venv/bin/activate

echo "[3/3] 安装依赖..."
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

echo ""
echo "========================================"
echo "启动后端服务..."
echo "========================================"
echo "服务地址: http://localhost:8000"
echo "API 文档: http://localhost:8000/docs"
echo ""
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
