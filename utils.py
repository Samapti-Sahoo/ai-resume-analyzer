import PyPDF2
import re
from skill_data import skills

def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

def extract_skills(text):
    found_skills = []
    for skill in skills:
        if skill in text:
            found_skills.append(skill)
    return found_skills
