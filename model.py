from transformers import pipeline

classifier = pipeline("zero-shot-classification")

candidate_labels = [
    "Vague/Unverifiable",
    "Fact-Based/Certified",
    "Marketing Fluff",
    "Evidence-Based"
]

def classify_text(text):
    try:
        result = classifier(
            text,
            candidate_labels,
            hypothesis_template="This statement is {}."
        )
        return result
    except:
        return {"labels": ["Unknown"], "scores": [0.0]}