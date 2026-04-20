# KNN 실질적으로 구현
import chromadb

import pandas as pd
from sentence_transformers import SentenceTransformer

df = pd.read_csv("todo_data.csv")
print(df.head())
contents = list(df["content"])
categories = list(df["category"])

model = SentenceTransformer("jhgan/ko-sroberta-multitask")
vectors = model.encode(contents).tolist()

client = chromadb.Client()

collection = client.create_collection(
    name="todo_collection",
    metadata={'hnsw:space': "cosine"}
)

collection.add(
    ids=[str(i) for i in range(len(vectors))],
    embeddings=vectors,
    documents=contents,
    metadatas=[{"category":category} for category in categories]
)

# 새로운 할 일을 입력했을때
# 카테고리 분류를 예측해줌 -> 벡터값을 통해서 -> 가장 유사한 벡터값들(k개)로 인해
def classify_todo(todo_content, k=3):
    # content를 벡터로 변환
    todo_content_vector = model.encode(todo_content)
    results = collection.query(
        query_embeddings=todo_content_vector,
        n_results=k,
        include=["documents", "metadatas", "distances"]
    )
    neighbors = results["metadatas"][0]
    distances = results["distances"][0]
    documents = results["documents"][0]

    votes = {}
    for neighbor, dist in zip(neighbors, distances):
        cat = neighbor["category"]
        similarity = 1 - dist
        votes[cat] = votes.get(cat, 0) + similarity
    predicted = max(votes, key=votes.get)

    return {
        "input": todo_content,
        "documents": documents,
        "predicted":predicted,
        "votes":votes
    }

result = classify_todo("육아하기")
print(f"예측 : {result['predicted']}")
print(f"근거 : {result['votes']}")