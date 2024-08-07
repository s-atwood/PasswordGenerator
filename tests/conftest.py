import pytest

# test_passphrase
word_list = ["random", "sample", "words"]

@pytest.fixture
def two_word_passphrase():
    words = word_list
    indices = [0,2]
    yield words, indices

@pytest.fixture
def single_word_passphrase():
    words = word_list
    indices = [1]
    yield words, indices

@pytest.fixture
def empty_passphrase():
    words = []
    indices = [0]
    yield words, indices

@pytest.fixture
def whole_list_passphrase():
    words = word_list
    indices = list(range(len(word_list)))
    yield words, indices