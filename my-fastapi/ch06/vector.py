from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

todos = [
    "피트니스 동아리 열심히 참여하기",
    "전공동아리 월말 보고서 작성하기",
    "약 먹기",
    "fast-api 공부하기",
    "조현우와 함께 귀가"
]


vectors = model.encode(todos)
print(f"벡터 크기 : {vectors.shape}")

sim_matrix = cosine_similarity(vectors)
for i, todo in enumerate(["피트니스", "보고서", "약", "공부", "조현우"]):
    row = sim_matrix[i, :]
    print(f"{todo} : {row}")

