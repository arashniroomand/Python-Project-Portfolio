import string 
import random
import nltk

nltk.download('words')


def generate_random_password(lenght = 8, include_numbers = False, include_symbols = False):
    """
    Generate a random password using the specified options.
    :param lenght: The length of the password.
    :param include_numbers: Whether to include numbers in the password.
    :param include_symbols: Whether to include symbols in the password.
    :return: The generated password.
    """
    if include_numbers:
        character = string.ascii_letters + string.digits
    elif include_symbols:
         character = string.ascii_letters + string.punctuation
    else: 
        character = string.ascii_letters
    
    return ''.join([random.choice(character) for _ in range(lenght)])


def generate_memorable_password(
    no_words,
    separator = '--',
    capitalzation: bool = False,
    vocabulary = None
    ):
    """
    Generates a memorable password consisting of a specified number of words, separated by a custom separator, with optional capitalization.

    Args:
        no_words (int): The number of words to include in the password.
        separator (str, optional): The separator to use between the words. Defaults to '--'.
        capitalzation (bool, optional): Whether to capitalize the first letter of each word. Defaults to False.
        vocabulary (list, optional): The list of words to choose from. Defaults to the NLTK corpus of English words.

    Returns:
        str: The generated memorable password.
    """
    
    if vocabulary is None:
        vocabulary = nltk.corpus.words.words()
        
    if capitalzation:
        return separator.join([random.choice(vocabulary).capitalize() for _ in range(no_words)])
    else:
        return separator.join([random.choice(vocabulary) for _ in range(no_words)])


def generate_pin_password(lenght = 4):
    """
    Generates a random PIN password consisting of a specified number of digits.

    Args:
        lenght (int): The length of the PIN password.

    Returns:
        str: The generated PIN password.
    """
    return ''.join([random.choice(string.digits) for _ in range(lenght)])

if __name__ == '__main__':
    print(generate_random_password(lenght = 10, include_numbers = True, include_symbols = True))
    print(generate_memorable_password(no_words = 3))
    print(generate_pin_password(lenght = 4))