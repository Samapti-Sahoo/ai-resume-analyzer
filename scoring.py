from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text, job_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    return float(similarity[0][0])

def calculate_final_score(similarity, skill_match_ratio, ats_score):
    final_score = (0.5 * similarity * 100) + (0.3 * skill_match_ratio * 100) + (0.2 * ats_score)
    return round(final_score, 2)
