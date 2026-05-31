import random
from runnableabstract import Runnable


class RealLLM(Runnable):
    def __init__(self):
        print("Initializing PseudoLLM...")

    def invoke(self, input_data):
        responses_bucket_list = [
            'New Delhi is capital of India.',
            'The Great Wall of China is one of the Seven Wonders of the World.',
            'The Amazon rainforest is the largest tropical rainforest in the world.',
        ]
        return random.choice(responses_bucket_list)

    