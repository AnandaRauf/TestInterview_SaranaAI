from transformers import pipeline

class GeminiModel:
    def __init__(self):
        self.pipeline = pipeline('text-classification', model='bert-base-uncased')  # Placeholder untuk Gemini

    def predict(self, text):
        return self.pipeline(text)
