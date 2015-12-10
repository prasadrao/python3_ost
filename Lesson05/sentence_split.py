import re

def sentence_split(text):
    return re.split(r"[?.!]\s+", text)

if __name__ == "__main__":
    print(sentence_split("Hello! My name is Steve. What is yours? I hope you enjoyed this class!"))
