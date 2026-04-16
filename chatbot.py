            #SMART CHATBOT IN PYTHON USING NLP(Natural language processing)

import random
import nltk
from nltk.stem import PorterStemmer
from data import data

#initialize NLTK and download required resources
#nltk.download("punkt")
#nltk.download("punkt_tab")
stemmer = PorterStemmer()


#Map intent categories to theri corresponding response categories
INTENT_RESPONSE_MAP = {
    "greetings": "greeting_responses",
    "farewells": "farewell_responses",
    "questions": "question_responses",
    "small_talk": "small_talk_responses",
    "thanks": "thanks_responses"
}

def preprocess(sentence):
    tokens = sentence.lower().split()
    return [stemmer.stem(token) for token in tokens]


def get_response(user_input):
    processed_input = preprocess(user_input)

    #check for all the pattern categories
    for intent_category, response_category in INTENT_RESPONSE_MAP.items():
        for pattern in data[intent_category]:
            processed_pattern = preprocess(pattern)
            if all(word in processed_input for word in processed_pattern):
                return random.choice(data[response_category])
            
    #fall back for unknown inputs
    return "SORRY!! I'm not able to respond that.Could you rephrase that sentence again??"

def chat():
    print("Chatbot: I am your chatbot here.Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!Have a great day.")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chat()