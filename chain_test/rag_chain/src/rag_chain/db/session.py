from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from rag_chain.core.config import settings
from .models import Vector  # 假设你的模型名为 Vector

engine = create_engine(settings.database_uri)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_vector_by_id(vector_id: int):
    """
    根据提供的向量 ID 从数据库检索向量。
    
    参数:
    - vector_id (int): 要检索的向量的 ID。
    
    返回:
    - VectorModel 实例，如果找到对应的向量；否则返回 None。
    """
    db: Session = SessionLocal()
    try:
        return db.query(Vector).filter(Vector.id == vector_id).first()
    finally:
        db.close()

def create_vector(vector_data: dict):
    """
    创建一个新的向量并存储在数据库中。
    
    参数:
    - vector_data (dict): 包含向量描述和值的字典。
    
    返回:
    - 创建的 VectorModel 实例。
    """
    db = SessionLocal()
    try:
        # 创建一个新的 Vector 实例
        vector = Vector(**vector_data)
        db.add(vector)
        db.commit()
        db.refresh(vector)  # 重新加载实例以获取分配的 ID 等
        return vector
    finally:
        db.close()

def update_vector(vector_id: int, vector_data: dict):
    """
    更新数据库中的特定向量。
    
    参数:
    - vector_id (int): 要更新的向量的 ID。
    - vector_data (dict): 包含更新数据的字典。
    
    返回:
    - 更新后的 VectorModel 实例，如果找到并成功更新；否则返回 None。
    """
    db = SessionLocal()
    try:
        vector = db.query(Vector).filter(Vector.id == vector_id).first()
        if vector:
            for key, value in vector_data.items():
                setattr(vector, key, value)
            db.commit()
            db.refresh(vector)
            return vector
        return None
    finally:
        db.close()

