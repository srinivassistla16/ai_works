import random

class PseudoLLM:
    def __init__(self):
        print("Initializing PseudoLLM...")

    def predict(self, prompt):
        responses_bucket_list = [
            'New Delhi is capital of India.',
            'The Great Wall of China is one of the Seven Wonders of the World.',
            'The Amazon rainforest is the largest tropical rainforest in the world.',
        ]
        return random.choice(responses_bucket_list)
    