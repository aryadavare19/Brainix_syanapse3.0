🌱 Project Overview

Green-Truth Auditor (ClaimSense) is an AI-powered tool that analyzes sustainability claims of products and brands. It helps users detect “greenwashing,” vague claims, and verify certified sustainability claims using a combination of:

NLP-based classification (Zero-Shot Text Classification)
Buzzword detection (vague sustainability terminology)
RAG-based brand verification (checking official certifications)
Hybrid reasoning (confidence and risk scoring)

The tool supports two input modes:

Text Input: Users enter a product description manually.
URL Input: Users provide a product URL, and the system extracts the relevant text for analysis.

The system combines these features to give a final decision, risk score, and AI reasoning for the sustainability claims.

🛠️ Features
1️⃣ Text Input
Input a product description.
Detects sustainability-related buzzwords.
Checks if the description contains strong evidence (e.g., certifications, measurable claims).
Runs AI model classification to support claim verification.
Provides final decision, confidence score, risk score, highlighted text, and reasoning.
2️⃣ URL Input
Enter a product page URL.
Scrapes relevant text using BeautifulSoup, removing menus, footers, and non-content elements.
Performs the same analysis pipeline as the text input mode.
Provides content preview and analysis results.
🔗 Additional Features
Buzzword highlighting in analyzed text.
Hybrid confidence scoring combining model predictions, evidence, and certification results.
Greenwashing Risk Score (0–100 scale).
Key extracted sentences for readability.
Modern Streamlit UI with radio button input selection and clear results layout.
🗂️ Project Structure
ClaimSense/
│
├─ app.py                  # Main Streamlit app
├─ scraper.py              # URL text extraction logic
├─ model.py                # NLP model (zero-shot classification)
├─ buzzwords.py            # Buzzword and strong evidence detection
├─ rag.py                  # Brand certification checker
├─ reasoning.py            # AI reasoning generation
├─ brands.csv              # Dataset of brands and certifications
├─ labels.py               # Descriptions of classification labels
├─ requirements.txt        # Python dependencies
└─ README.md               # Project documentation
🧰 Dependencies

Install Python dependencies with:

pip install -r requirements.txt

requirements.txt

streamlit
requests
beautifulsoup4
pandas
transformers
torch
🚀 How to Run
Open terminal in the project folder.
Run Streamlit app:
streamlit run app.py
The app will open in your browser at:
http://localhost:8501
Choose input type: Text or URL.
Enter your description or URL and click Analyze.
View:
Buzzwords detected
Model classification
Certification check
Final decision
Greenwashing risk score
AI reasoning
Highlighted analyzed text
Key extracted sentences
🔍 Testing URLs

Use the following sample product URLs for testing the URL input:

https://earthhero.com/products/reusable-beeswax-wraps
https://brownliving.in/products/organic-cotton-tshirt
https://letsbeco.com/collections/home-cleaning/products/eco-friendly-cleaner
https://prakati.in/products/plant-based-soap
https://www.ecohoy.com/products/biodegradable-straws

⚠️ Note: Only direct product pages work reliably for scraping text.

🧠 Technical Workflow
Input Handling
If Text, take user input.
If URL, fetch and clean page content.
Buzzword Detection
Detect common vague sustainability keywords.
Evidence Detection
Identify measurable claims, certifications, and verified data.
RAG (Brand Certification Check)
Match brand names in the text against brands.csv to find official certifications.
Zero-Shot Classification
Classify text into labels: Fact-Based/Certified, Marketing Fluff, Vague/Unverifiable, Evidence-Based.
Hybrid Confidence
Combine model confidence with presence/absence of buzzwords, evidence, and certification.
Final Decision & Scoring
Generate final verdict.
Compute Greenwashing Risk Score.
Highlight buzzwords in analyzed text.
Extract key sentences.
Provide AI reasoning.
UI Presentation
Clean layout with Streamlit radio buttons, progress bars, and highlighted results.
💡 How to Present the Two Features Technically
✅ 1. Text Input Feature
Explain that the user directly enters a product description.
Show live text analysis:
Buzzwords detected
AI model support classification
Evidence and certification check
Highlighted words
Emphasize how short or vague text triggers warnings.
✅ 2. URL Input Feature
Explain that the user inputs a product URL.
The scraper extracts clean product content, ignoring headers, footers, menus.
Demonstrate the same analysis workflow as text input.
Show the extracted content preview and processed results.
Emphasize real-time integration of web scraping with AI + RAG analysis.
💻 Key Technical Points for Presentation
Integration of two input modes: unified pipeline ensures all content goes through the same detection/classification logic.
Hybrid AI + RAG + Heuristics:
NLP zero-shot model classifies text.
Buzzwords + evidence heuristics adjust confidence.
Certification lookup verifies official claims.
Explainable Outputs:
Highlighted buzzwords in text.
Key sentences.
Risk scores with thresholds (High, Medium, Low).
Streamlit UI:
Intuitive input selection (radio buttons)
Visual progress bar for confidence
Subsections for clarity
Scrollable product text preview

Tip: During demo, you can compare Text vs URL input using the same product to show consistency and hybrid analysis effectiveness.

📝 Optional Improvements
Add multi-page UI: one for Text, one for URL.
Include product images in the preview.
Add downloadable PDF reports for analysis.
Implement batch URL input for analyzing multiple products at once.
Visualize buzzword frequency or risk score distribution.
