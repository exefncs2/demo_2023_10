CREATE DATABASE prefect;

CREATE ROLE prefect_role;

-- 授予角色 "prefect_role" 超级用户权限（最大权限）
ALTER ROLE prefect_role SUPERUSER;

-- 授予角色 "prefect_role" 创建数据库的权限
ALTER ROLE prefect_role CREATEDB;

-- 授予角色 "prefect_role" 连接到数据库的权限
ALTER ROLE prefect_role CONNECTION LIMIT -1;

-- 创建一个用户 "prefect" 并设置密码，并分配给角色 "prefect_role"
CREATE USER prefect WITH PASSWORD 'prefect';
GRANT prefect_role TO prefect;

