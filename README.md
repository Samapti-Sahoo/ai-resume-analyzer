# 🚀 AI Resume Analyzer  
### Intelligent Job Matching & ATS Compatibility System  

An AI-powered web application that analyzes resumes against job descriptions using Natural Language Processing (NLP) techniques and provides a detailed match score, skill gap analysis, and ATS compatibility evaluation.

🔗 **Live App:** https://ai-resume-analyzer-h7ymlmw9evp6nfybyfc676.streamlit.app  
💻 **GitHub Repository:** https://github.com/Samapti-Sahoo/ai-resume-analyzer  

---

## 📌 Problem Statement

Recruiters receive hundreds of resumes for a single job role. Manual screening is time-consuming and biased. Additionally, many candidates do not know how well their resume matches a job description or whether it passes ATS (Applicant Tracking System) filters.

This project automates resume evaluation and provides intelligent feedback using NLP-based similarity analysis.

---

## 🧠 Features

- 📄 Resume Upload (PDF)
- 📝 Job Description Analysis
- 📊 Resume Match Score (0–100%)
- 🎯 Skill Gap Detection
- 🤖 ATS Compatibility Checker
- 📈 Visual Dashboard (Charts & Metrics)
- ⚡ Real-time Analysis

---

## ⚙️ Tech Stack

**Frontend & Deployment**
- Streamlit
- Streamlit Cloud

**Backend & NLP**
- Python
- scikit-learn (TF-IDF, Cosine Similarity)
- spaCy
- PyPDF2

**Visualization**
- Matplotlib

---

## 🧮 Algorithm Used

1. Text Preprocessing
   - Lowercasing
   - Stopword removal
   - Tokenization

2. Feature Extraction
   - TF-IDF Vectorization

3. Similarity Calculation
   - Cosine Similarity

4. Final Resume Score Formula:Final Score =
50% Similarity Score +
30% Skill Coverage +
20% ATS Compatibility

---

## 🏗 System Architecture

User Upload  
↓  
PDF Text Extraction  
↓  
Text Cleaning  
↓  
Skill Extraction  
↓  
TF-IDF Vectorization  
↓  
Cosine Similarity  
↓  
Score Calculation  
↓  
Dashboard Visualization  

---

## 📊 Output Example

- Resume Match Score: 82%
- Matched Skills
- Missing Skills
- ATS Score
- Visual Skill Distribution Chart
## 🚀 How to Run Locally

```bash
git clone https://github.com/Samapti-Sahoo/ai-resume-analyzer.git
cd ai-resume-analyzer
pip install -r requirements.txt
streamlit run app.py


Future Improvements

1.Semantic similarity using BERT

2.Multi-language resume support

3.Downloadable PDF report

4.LinkedIn profile integration

5.Bulk resume analysis for recruiters


Author

Samapti Sahoo
AI & ML Enthusiast
Deployed on Streamlit Cloud
