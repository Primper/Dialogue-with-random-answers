import nltk
from nltk import edit_distance
import random

# Below is a list of phrases 
PHRASES_CONFIG = {
    "options": {
        "hello": {
            "request":  ["hello", 
                         "hi", 
                         "hey", 
                         "hi there", 
                         "hey there", 
                         "hey man", 
                         "hey bro", 
                         "hey girl", 
                         "hey dude", 
                         "hey buddy", 
                         "yo", 
                         "howdy"],
                        ######################################
            "response": ["Nice to see you!", 
                         "It's nice to see you again!", 
                         "Good to see you!", 
                         "Nice to meet you!", 
                         "Hello", 
                         "Hi", 
                         "Hey", 
                         "Hi there", 
                         "Hey there", 
                         "Hey dude", 
                         "Yo", 
                         "Howdy"]
        },
        "thanks": {
            "request":  ["thanks", 
                         "thank you"],
                        ######################################
            "response": ["You're welcome",
                         "No problem",
                         "No worries",
                         "Don't mention it",
                         "My pleasure",
                         "Anytime",
                         "It was the least I could do",
                         "Glad to help",
                         "Sure!"]
        },
        "howareu": {
            "request":  ["how are you doing?",
                         "how have you been?",
                         "how's everything?",
                         "how's it going?",
                         "how are things going?",
                         "how are you",
                         "what's going on?",
                         "what's new?",
                         "what's up?",
                         "whassup?",
                         "what are you up to?"],
                        ######################################
            "response": ["I'm good",
                         "Pretty good",
                         "I'm well",
                         "I'm OK",
                         "Not too bad",
                         "Same old, same old",
                         "All right",
                         "I'm ALIVE"]
        }
    }
}

def get_option(input_text):
    # We go through the OPTIONS for all keys
    for option in PHRASES_CONFIG["options"].keys():
        # We go through all REQUESTS
        for request in PHRASES_CONFIG["options"][option]["request"]:
            # Assign input and output texts
            text1 = alphabet(input_text.lower())
            text2 = alphabet(request.lower())
            # and check if the text is correct
            if edit_distance(text1, text2) / max(len(text1), len(text2)) < 0.3:
                return option # If the match is less than 0.3, then program will not understand the text
    return "Not found"

def alphabet(text):
    output_text = ""
    for char in text: # Go through each character of text
        # If the character is found in the string, 
        if char in "qwertyuiopasdfghjklzxcvbnm" or "1234567890" or "`!@#$%^&*()_+-=~';/.,":
            output_text = output_text + char  # then we add it to the OUTPUT_TEXT variable
    return output_text

def response_rand(input_text):
    # The function gets the value of the input text
    option = get_option(input_text)
    if option == "Not found":  
        # If the text value does not match
        return "I do not understand you"
    else:
        # If it matches, then choose a random phrase from the corresponding option RESPONSE
        return random.choice(PHRASES_CONFIG["options"][option]["response"])

print("Write something")
print("OR")
print("To exit the dialog write: Exit")
print("____________________________________\n")

while True:
    input_text = input()
    if input_text == "": # If we wrote an exit, then the exit from the program
        print("You didn't write anything")
    elif input_text.lower() == "exit":  # If we didn't write anything
        break
    else:
        print(response_rand(input_text))  # Otherwise print the answer
