# ✅ Buzzwords list (with variations)
buzzwords = [
    "eco-friendly", "ecofriendly", "green", "natural", "organic",
    "sustainable", "environmentally friendly",
    "eco-conscious", "non-toxic", "clean",
    "earth-friendly", "chemical-free",
    "plant-based", "pure", "safe"
]

# 🔍 Detect buzzwords (handles variations)
def detect_buzzwords(text):
    found = []
    text_lower = text.lower().replace("-", "").replace(" ", "")

    for word in buzzwords:
        word_clean = word.replace("-", "").replace(" ", "")
        if word_clean in text_lower:
            found.append(word)

    return list(set(found))

# 🧠 Strong evidence detection
def has_strong_evidence(text):
    keywords = [
        "certified", "gots", "fsc", "fair trade", "b-corp",
        "carbon", "footprint", "emissions", "net zero",
        "recycled", "organic cotton", "biodegradable",
        "compostable", "sugarcane", "tencel", "lyocell",
        "merino wool", "verified", "standard", "approved"
    ]

    text_lower = text.lower()
    return any(k in text_lower for k in keywords)

def hasonlybuzzwords(text, buzz):
    textlower = text.lower()

    for word in buzz:
        textlower = textlower.replace(word, "")

    # remove common filler words
    fillers = ["the", "and", "is", "are", "with", "for", "this", "that", "our"]
    for f in fillers:
        textlower = textlower.replace(f, "")

    return len(textlower.strip()) < 50
