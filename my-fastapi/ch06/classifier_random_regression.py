import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("/Users/j1w0n9/AI_Platform/my-fastapi/ch06/todo_data.csv")

contents = df["content"]
categories = df["category"]

X_train, X_test, Y_train, Y_test = train_test_split(
    contents, categories, test_size=0.2, random_state=42
)

embed_model = SentenceTransformer("jhgan/ko-sroberta-multitask")
X_train_embedding = embed_model.encode(list(X_train))
X_test_embedding = embed_model.encode(list(X_test))

lr_model = LogisticRegression()
lr_model.fit(X_train_embedding, Y_train)
lr_pred = lr_model.predict(X_test_embedding)
lr_acc = (lr_pred == Y_test).mean()
print(f"로지스틱 회귀 정확도: {lr_acc}")

def classify_content(text: str) -> dict:
    vectors = embed_model.encode([text])
    predicted_categories = lr_model.predict(vectors)[0]
    probabilities = lr_model.predict_proba(vectors)[0]
    category_label = lr_model.classes_

    prob_dict = {
        label: round(float(prob) * 100, 2) for label, prob in zip(category_label, probabilities)
    }

    return {
        "input" : text,
        "predicted_category" : predicted_categories,
        "probability" : prob_dict
    }

if __name__ == "__main__":
    test_contents = [
        "하교하기",
        "전공동아리 월말 보고서 제출",
        "수학여행 물품사기"
    ]

    for content in test_contents:
        result = classify_content(content)
        print(result)