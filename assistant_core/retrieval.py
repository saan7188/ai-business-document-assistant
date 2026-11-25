from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class DocumentIndex:
    def __init__(self, passages):
        if not passages:
            raise ValueError("No readable text found")
        self.passages = passages
        self.vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
        self.matrix = self.vectorizer.fit_transform([text for _, text in passages])

    def search(self, question, limit=4):
        scores = cosine_similarity(self.vectorizer.transform([question]), self.matrix)[0]
        order = scores.argsort()[::-1][:limit]
        return [(self.passages[i][0], self.passages[i][1], float(scores[i])) for i in order if scores[i] > 0]
