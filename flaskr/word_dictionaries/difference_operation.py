import json
from pathlib import Path

all_words_path = Path('./words_dictionary.json')
common_words_path = Path('./common.json')

def load_all_words(file_path):
    try:
        with open(file_path, 'r') as file:
            all_words_dict = json.load(file)

        return set(all_words_dict.keys())
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return set()

def load_common_words(file_path):
    try:
        with open(file_path, 'r') as file:
            common_words_dict = json.load(file)

        common_words_list = common_words_dict['commonWords']

        return set(common_words_list)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return set()

def filter_common_words():
    all_words_set = load_all_words(all_words_path)
    common_words_set = load_common_words(common_words_path)

    return all_words_set - common_words_set