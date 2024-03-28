# rag_chain/db/__init__.py

from .session import SessionLocal
from .models import Vector  # 假设你有一个Vector模型

def get_all_vectors():
    """检索数据库中所有向量的简化示例"""
    # 创建一个新的数据库会话实例
    db = SessionLocal()
    try:
        # 查询所有Vector记录
        vectors = db.query(Vector).all()
        return vectors
    finally:
        # 关闭会话
        db.close()

