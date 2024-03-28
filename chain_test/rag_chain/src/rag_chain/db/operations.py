# rag_chain/db/operations.py

from sqlalchemy.orm import Session
from . import models

def get_all_vectors(db: Session):
    return db.query(models.Vector).all()

def get_vector_by_id(db: Session, vector_id: int):
    return db.query(models.Vector).filter(models.Vector.id == vector_id).first()

def create_vector(db: Session, vector_data: dict):
    db_vector = models.Vector(**vector_data)
    db.add(db_vector)
    db.commit()
    db.refresh(db_vector)
    return db_vector

def update_vector(db: Session, vector_id: int, vector_data: dict):
    db_vector = db.query(models.Vector).filter(models.Vector.id == vector_id).first()
    if db_vector:
        for key, value in vector_data.items():
            setattr(db_vector, key, value)
        db.commit()
        db.refresh(db_vector)
    return db_vector

def delete_vector(db: Session, vector_id: int):
    db_vector = db.query(models.Vector).filter(models.Vector.id == vector_id).first()
    if db_vector:
        db.delete(db_vector)
        db.commit()
    return db_vector

