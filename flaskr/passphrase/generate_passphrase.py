def generate_passphrase(words, indices):
    passphrase_words = [words[index] for index in indices]
    passphrase = '-'.join(passphrase_words)
    return passphrase