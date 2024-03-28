# 指定基础镜像
FROM python:latest

# 设置工作目录
WORKDIR /work

# 复制项目文件到镜像中
COPY . /work

# 安装依赖项
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口
EXPOSE 8080

# 运行 FastAPI 服务
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080" ]
