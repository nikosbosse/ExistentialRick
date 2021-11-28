from create_api import create_api
import pandas as pd
import time
import random
import tweepy

class existentialrick:    

    def __init__(self):
        self.url = "https://forum.effectivealtruism.org/allPosts"

    def get_random_word(self): 
        data = pd.read_csv('random-words.txt', header=None, dtype=str)
        self.word = data[0].sample(n = 1).item().title()


    def write_tweet(self):
        message = [
            f'{self.word} is an existential risk'
            ]
        message = " \n".join(message)
        return message