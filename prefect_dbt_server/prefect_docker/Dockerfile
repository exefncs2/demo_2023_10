# 指定基础镜像
FROM python:latest

# 设置工作目录
WORKDIR /work

#變數

# 复制项目文件到镜像中
COPY ./demo /work/demo
COPY ./requirements.txt /work/requirements.txt
COPY ./prefect /work/prefect
COPY ./start.sh /work/start.sh
COPY ./add_flow.sh /work/add_flow.sh

# 安装依赖项
RUN pip install --no-cache-dir -r ./requirements.txt

# 暴露端口
EXPOSE 5432
EXPOSE 4200


