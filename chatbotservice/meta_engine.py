'''

Author: Ming Yeh Oliver Cheung

Copyright (c) 2021 Wise CSE Group 1
'''
import logging, random, os 
from nlp_engine import NlpEngine

SEP = os.path.sep

class MetaEngine:

    def __init__(self):
        """ initialises Meta-engine with all necessary components
        """
        logging.info("Started Meta Engine...")
        self.nlp = NlpEngine("models" + SEP + "onlineshop")
        self.actions = {"Fun_Fact": 
                            ["Google has the largest index of websites in the world.",
                            "The original name of Google was Backrub.",
                            "The Google search technology is called PageRank."],
                        "Recommendation": self.get_recommendations(),
                        "Welcome":
                            ["Hello there!", 
                            "Hi!",
                            "Welcome to our amazing online shop!",
                            "Beautiful day isn't it?",
                            "Feels like a perfect day for online shopping!",],
                        None: ["I'm sorry coulnd't quite understand you there, mind rephrasing that for me?",
                                "Currently I'm not smart enough for that yet but I'll try my best to improve!",
                                "I'm sorry, I didn't understand that."]}

    def handle_message(self, text):
        """ Gets classification of user input and chooses appropriate return message

        Args:
            text (str): Input message from User

        Returns:
            [str]: message that is randomly chosen from self.actions and send to you user
        """
        user_action = self.nlp.textcat(text)
        messages = self.actions.get(user_action)
        random.shuffle(messages)
        return messages[0]

    def get_recommendations(self):
        """ Gets recommendations from recommendationservice
        """
        #TODO
        return["shoes","camera","laptop"]

if __name__ == "__main__":
    """For quick local testing purposes only!"""
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
                        filename="logs.txt",
                        datefmt='%d/%m/%Y %I:%M:%S %p',
                        filemode='w', level=logging.DEBUG)

    engine = MetaEngine()

    while True:
        message = input("Please enter something: ")
        print(engine.handle_message(message))

