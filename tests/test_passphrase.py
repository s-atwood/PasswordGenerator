from flaskr.passphrase.generate_passphrase import generate_passphrase
import pytest


def describe_generate_passphrase():

    def describe_joining_words():

        @pytest.mark.usefixtures('two_word_passphrase')
        def it_joins_two_words_with_hyphen(two_word_passphrase):
            words, indices = two_word_passphrase
            expected_output = 'random-words'
            assert(
                generate_passphrase(words, indices) == expected_output
            ), f'Expected {expected_output},but got {generate_passphrase(words, indices)}'

        @pytest.mark.usefixtures('single_word_passphrase')
        def it_makes_single_word_passphrase(single_word_passphrase):
            words, indices = single_word_passphrase
            expected_output = 'sample'
            assert(
                generate_passphrase(words, indices) == expected_output
            ), f'Expected {expected_output}, but got {generate_passphrase(words, indices)}'

        @pytest.mark.usefixtures('empty_passphrase')
        def it_makes_empty_passphrase(empty_passphrase):
            words, indices = empty_passphrase
            if words:
                expected_output = ''
                assert(
                    generate_passphrase(words, indices) == expected_output
                ), f'Expected {expected_output}, but got {generate_passphrase(words, indices)}'

        @pytest.mark.usefixtures('whole_list_passphrase')
        def it_makes_whole_list_passphrase(whole_list_passphrase):
            words, indices = whole_list_passphrase
            expected_output = 'random-sample-words'
            assert(
                generate_passphrase(words, indices) == expected_output
            ), f'Expected {expected_output}, but got {generate_passphrase(words, indices)}'