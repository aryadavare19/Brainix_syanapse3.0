import requests
from bs4 import BeautifulSoup
import re

KEYWORDS = [
    "material", "made", "fabric", "sustainable", "recycled",
    "organic", "cotton", "plastic", "features", "benefits",
    "eco", "carbon", "footprint", "design", "technology",
    "certified", "ingredients", "composition"
]

def clean_text(text):
    text = re.sub(r'(\b\w\b\s?){3,}', lambda m: m.group(0).replace(" ", ""), text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_text_from_url(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=8)
        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup(["script", "style", "nav", "footer", "header", "button", "aside"]):
            tag.extract()

        texts = []

        for tag in soup.find_all(["p", "li", "div"]):
            text = tag.get_text(separator=" ", strip=True)
            text = clean_text(text)

            if (
                len(text) > 60 and
                any(keyword in text.lower() for keyword in KEYWORDS) and
                "free shipping" not in text.lower() and
                "returns" not in text.lower() and
                "cart" not in text.lower() and
                "sale" not in text.lower()
            ):
                texts.append(text)

        content = " ".join(texts)

        if len(content) < 150:
            return None

        return content[:3000]

    except Exception:
        return None