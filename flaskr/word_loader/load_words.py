import json
from pathlib import Path

FILE_PATH = Path('english_corpus2.json')


def load_words_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            words = json.load(file)
        return words
    except FileNotFoundError:
        print(f"File '{FILE_PATH}' not found.")
        return list()

words = load_words_from_json(FILE_PATH)
print(type(words))