import streamlit as st
from scraper import extract_text_from_url
from model import classify_text
from buzzwords import detect_buzzwords, has_strong_evidence, hasonlybuzzwords
from rag import check_certification
from reasoning import generate_reasoning

# 🌱 Page Config
st.set_page_config(page_title="Green-Truth Auditor", layout="wide")

# 🌱 Title


st.title("🌱 Green-Truth Auditor 1")
st.markdown(
    "AI-powered Green Claim Verification System — Analyze sustainability claims of products and brands."
)
st.markdown("---")

# 🔘 Input Type Selection
option = st.radio("Choose Input Type", ["Text", "URL"], horizontal=True)

user_input = ""
url = ""

# Input area
if option == "Text":
    user_input = st.text_area("Enter product description", height=150)
else:
    url = st.text_input("Enter product URL", placeholder="https://www.example.com/product")

# Analyze Button
if st.button("Analyze"):
    # 🌐 URL handling
    if option == "URL":
        if not url.strip():
            st.warning("Please enter a URL")
            st.stop()

        user_input = extract_text_from_url(url)
        if not user_input:
            st.error("Failed to fetch content from URL or content too short")
            st.stop()

        st.subheader("🌐 Extracted Content Preview")
        st.write(user_input[:500] + "...")
        st.markdown("---")

    # ❌ Empty input
    if not user_input.strip():
        st.warning("Enter some text to analyze")
        st.stop()

    # 🚨 Handle very short text
    if len(user_input.strip()) < 15:
        st.subheader("🔴 Likely Greenwashing – Too Vague")
        st.write("Input is too short and contains vague sustainability wording.")
        st.stop()

    # 🔍 Buzzwords Detection
    buzz = detect_buzzwords(user_input)

    # 🧠 Strong Evidence Detection
    evidence = has_strong_evidence(user_input)

    # 📊 Certification Check
    rag_result = check_certification(user_input)

    # 🚨 Only buzz check
    only_buzz = hasonlybuzzwords(user_input, buzz)

    # 🤖 Model Classification
    result = classify_text(user_input)
    label = result["labels"][0]
    confidence = result["scores"][0]

    # ⚖️ Penalty-based confidence adjustment
    penalty = 0
    if not evidence:
        penalty += 0.25
    if only_buzz:
        penalty += 0.25
    if not rag_result:
        penalty += 0.25

    confidence = max(0, confidence - penalty)

    if label == "Fact-Based/Certified" and not evidence:
        label = "Marketing Fluff"
    if confidence < 0.4:
        label = "Marketing Fluff"

    # 🎯 Final Decision Engine
    if rag_result:
        final_status = "✅ Verified Sustainable Brand"
    elif evidence and not rag_result:
        final_status = "🟡 Not Certified but Appears Genuine"
    elif buzz and not evidence:
        final_status = "🔴 Likely Greenwashing – Needs Verification"
    elif buzz and evidence:
        final_status = "⚠️ Mixed Claims (Check Further)"
    else:
        final_status = "⚠️ Insufficient Information"

    # 💡 Reasoning
    reasoning = generate_reasoning(final_status, buzz, evidence, rag_result)

    # 🔥 Greenwashing Risk Score
    risk_score = 0
    if buzz:
        risk_score += 50
    if not rag_result:
        risk_score += 30
    if confidence < 0.6:
        risk_score += 20

    # ================= UI Layout =================
    st.subheader("🚩 Buzzwords Detected")
    st.write(buzz if buzz else "None")

    st.subheader("🧠 Model Classification")
    st.write(f"{label} ({round(confidence, 2)})")
    st.progress(float(confidence))

    if rag_result:
        st.subheader("📊 Certification Found")
        st.write(rag_result)

    st.subheader("📢 Final Decision")
    st.write(final_status)

    st.subheader("⚠️ Greenwashing Risk Score")
    st.write(f"{risk_score}/100")
    if risk_score > 70:
        st.error("High Risk of Greenwashing")
    elif risk_score > 40:
        st.warning("Moderate Risk")
    else:
        st.success("Low Risk")

    st.subheader("💡 AI Reasoning")
    st.write(reasoning)

    # 📝 Highlight buzzwords in text
    highlighted_text = user_input
    for word in buzz:
        highlighted_text = highlighted_text.replace(
            word, f"🔴 {word.upper()} 🔴"
        )
    st.subheader("📝 Analyzed Text")
    st.write(highlighted_text)

    # 📄 Key Points
    st.subheader("📄 Key Extracted Sentences")
    sentences = user_input.split(".")
    for i, sentence in enumerate(sentences[:5]):
        if sentence.strip():
            st.write(f"{i+1}. {sentence.strip()}")

    st.markdown("---")
    st.caption("Built using AI + NLP + RAG for sustainability claim analysis 🌱")