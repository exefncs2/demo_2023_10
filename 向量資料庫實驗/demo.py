import pinecone      
import random
import string

# 計算公式
def hybrid_score_norm(dense, sparse, alpha: float):
    """Hybrid score using a convex combination

    alpha * dense + (1 - alpha) * sparse

    Args:
        dense: Array of floats representing
        sparse: a dict of `indices` and `values`
        alpha: scale between 0 and 1
    """
    if alpha < 0 or alpha > 1:
        raise ValueError("Alpha must be between 0 and 1")
    hs = {
        'indices': sparse['indices'],
        'values':  [v * (1 - alpha) for v in sparse['values']]
    }
    return [v * alpha for v in dense], hs


# 生成随机的不重复索引和对应的值
def generate_random_sparse_vector(length, min_value=0, max_value=1):
    indices = random.sample(range(length), random.randint(1, length))
    values = [random.uniform(min_value, max_value) for _ in range(len(indices))]
    return {'indices': indices, 'values': values}


# 生成随机的稠密向量
def generate_random_dense_vector(length, min_value=0, max_value=1):
    return [random.uniform(min_value, max_value) for _ in range(length)]

# 生成隨機文本
def generate_random_text(length):
    characters = string.ascii_letters + string.digits + string.punctuation + " "
    return ''.join(random.choice(characters) for _ in range(length))

# 連線
your_api_key=''
pinecone.init(      
	api_key=f'{your_api_key}',      
	environment='us-west4-gcp-free'      
)      


# 顯示所有index type:list 
print(pinecone.list_indexes())

# 獲取名為“test”的索引的配置和當前狀態：
print(pinecone.describe_index("test"))

# 使用者資訊
print(pinecone.whoami())


# 指定index 為test
index = pinecone.Index('test')

# index資訊
print(index.describe_index_stats())

random_text = generate_random_text(50)
print(random_text)
# 生成长度为100的随机不重复索引和值
sparse_vector = generate_random_text(50) #generate_random_sparse_vector(100)
sparse_vector2 = generate_random_sparse_vector(100)

# 限制向量(test目前為16)隨機索引直
dense_vector = generate_random_dense_vector(16)
dense_vector2 = generate_random_dense_vector(16)

# 插入資料
upsert_response = index.upsert(
    vectors=[
        {'id': 'vec1',
         'values': dense_vector,
         'metadata': {'genre': 'drama'},
         'sparse_values': sparse_vector
         },
        {'id': 'vec2',
         'values': dense_vector2,
         'metadata': {'genre': 'action'},
         'sparse_values': sparse_vector2
             }
    ],
    namespace='example-namespace'
)

# 查詢

# 生成长度为100的随机不重复索引和值
sparse_vector3 = generate_random_sparse_vector(100)

# 限制向量(test目前為16)隨機索引直
dense_vector3 = generate_random_dense_vector(16)

hdense, hsparse = hybrid_score_norm(dense_vector3, sparse_vector3, alpha=0.75)

query_response = index.query(
    namespace="example-namespace",
    top_k=10,
    vector=hdense,
    sparse_vector=hsparse
)

print(query_response)

# 範圍操作

# 搜尋
vec1 = index.fetch(["vec1"], namespace='example-namespace')
print(vec1)

# 更新
index.update(id="vec1", values=dense_vector2 , set_metadata={"type": "webdoc"})
vec1 = index.fetch(["vec1"], namespace='example-namespace')
print(vec1)

# 刪除
index.delete(ids=["vec2"], namespace='example-namespace')
vec2 = index.fetch(["vec2"], namespace='example-namespace')
print(vec2) #啪~沒了


# 輸出原始資料

print("###################DATA####################")
print(f"dense_vector:{dense_vector}",f"sparse_vector:{sparse_vector}")
print(f"------------------------------------------")
print(f"dense_vector2:{dense_vector2}",f"sparse_vector2:{sparse_vector2}")
print(f"------------------------------------------")
print(f"dense_vector3:{dense_vector3}",f"sparse_vector3:{sparse_vector3}")
print(f"------------------------------------------")