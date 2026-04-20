from transformers import pipeline

pipeline = pipeline("zero-shot-classification", "typeform/distilbert-base-uncased-mnli")

CATEGORIES = ["공부", "운동", "업무", "쇼핑"]

def predict_category(content : str) -> dict:
    result = pipeline(content, CATEGORIES)

    top_label = result["labels"][0]
    score_map = dict(zip(result["labels"], result["scores"]))

    return {
        "label": top_label,
        "score": score_map
    }

predict_category = predict_category("신발 사기")
print(predict_category)