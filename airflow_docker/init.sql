CREATE DATABASE airflow;

CREATE ROLE airflow_role;

-- 授予角色 "airflow_role" 超级用户权限（最大权限）
ALTER ROLE airflow_role SUPERUSER;

-- 授予角色 "airflow_role" 创建数据库的权限
ALTER ROLE airflow_role CREATEDB;

-- 授予角色 "airflow_role" 连接到数据库的权限
ALTER ROLE airflow_role CONNECTION LIMIT -1;

-- 创建一个用户 "airflow" 并设置密码，并分配给角色 "airflow_role"
CREATE USER airflow WITH PASSWORD 'airflow';
GRANT airflow_role TO airflow;

