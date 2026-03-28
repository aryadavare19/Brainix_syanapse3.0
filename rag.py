import pandas as pd
import re

# Load CSV
df = pd.read_csv("brands.csv")

def normalize(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text

def check_certification(text):
    text_clean = normalize(text)
    for _, row in df.iterrows():
        brand = row["brand"]
        brand_clean = normalize(brand)
        pattern = r'\b' + re.escape(brand_clean) + r'\b'
        if re.search(pattern, text_clean):
            return f"{brand} → {row['certification']}"
    return None