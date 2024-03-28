from fastapi import APIRouter, HTTPException, Path, Query
from typing import List
from rag_chain import text_processing, openai_integration, db
from ..schemas import VectorCreate, VectorUpdate, Vector, TextProcessRequest, GPTGenerateRequest

router = APIRouter()

@router.post("/vectors/", response_model=Vector)
async def create_vector(vector_create: VectorCreate):
    # 构造字典以匹配 Vector 模型的字段
    vector_data = {"description": vector_create.description}
    created_vector = db.session.create_vector(vector_data=vector_data)
    if not created_vector:
        raise HTTPException(status_code=400, detail="Vector could not be created.")
    return created_vector

@router.put("/vectors/{vector_id}", response_model=Vector)
async def update_vector(vector_id: int, vector_update: VectorUpdate):
    # 构造字典以匹配 Vector 模型的字段
    vector_data = {"description": vector_update.description}
    updated_vector = db.session.update_vector(vector_id=vector_id, vector_data=vector_data)
    if not updated_vector:
        raise HTTPException(status_code=404, detail="Vector not found.")
    return updated_vector

@router.delete("/vectors/{vector_id}")
async def delete_vector(vector_id: int):
    # 假设rag_chain提供了一个删除向量的函数
    result = db.session.delete_vector(vector_id=vector_id)
    if not result:
        raise HTTPException(status_code=404, detail="Vector not found.")
    return {"msg": "Vector deleted"}

# 假设我们还需要一个端点来处理文本，然后使用OpenAI生成某种输出
@router.post("/process-text/", response_model=Vector)
async def process_text(text: str):
    # 使用rag_chain的text_processing模块分割文本
    chunks = text_processing.chunk_text(text, chunk_size=512)
    # 假设使用OpenAI生成某种输出
    generated_text = openai_integration.openai_client.generate_text(chunks)
    if not generated_text:
        raise HTTPException(status_code=500, detail="Failed to generate text from OpenAI.")
    return {"description": generated_text}

# 假设还需要一个端点来获取所有向量
@router.get("/vectors/", response_model=List[Vector])
async def list_vectors():
    # 假设rag_chain提供了一个获取所有向量的函数
    vectors = db.get_all_vectors()
    if not vectors:
        raise HTTPException(status_code=404, detail="No vectors found.")
    return vectors
@router.post("/text/chunk", response_model=List[str], summary="将文本分割成块")
async def chunk_text(request: TextProcessRequest):
    # 文本分割的具体实现
    chunks = text_processing.chunk_text(request.text, request.chunk_size)
    return chunks

@router.post("/text/generate", response_model=str, summary="使用OpenAI GPT-3生成文本")
async def generate_text(request: GPTGenerateRequest):
    # 使用OpenAI GPT-3生成文本的具体实现
    generated_text = openai_integration.openai_client.generate_text(request.prompt)
    if not generated_text:
        raise HTTPException(status_code=500, detail="Failed to generate text.")
    return generated_text

@router.get("/vectors/{vector_id}", response_model=Vector, summary="获取指定ID的向量详情")
async def get_vector_by_id(vector_id: int = Path(..., description="The ID of the vector to get")):
    # 获取指定ID向量的具体实现
    vector = db.session.get_vector_by_id(vector_id)
    if not vector:
        raise HTTPException(status_code=404, detail="Vector not found.")
    return vector

@router.get("/text/analyze", response_model=dict, summary="对文本进行分析")
async def analyze_text(text: str = Query(..., description="The text to analyze")):
    # 文本分析的具体实现
    analysis_result = text_processing.analyze_text(text)
    return analysis_result
