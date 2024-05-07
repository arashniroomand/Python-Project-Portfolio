# Generating Secure and Memorable Passwords

## Overview
This code provides functions to generate random passwords with different characteristics. It offers flexibility in generating passwords with varying lengths, including numbers and symbols, and creating memorable passwords using words from a vocabulary.

## Random Password Generation
The `generate_random_password` function allows you to generate a random password with the following options:
- `length`: The desired length of the password.
- `include_numbers`: A boolean flag indicating whether to include numbers in the password.
- `include_symbols`: A boolean flag indicating whether to include symbols in the password.

Example usage:
```python
random_password = generate_random_password(length=10, include_numbers=True, include_symbols=True)
```

## Memorable Password Generation
The `generate_memorable_password` function creates a memorable password by combining a specified number of words separated by a custom separator. It also offers the option to capitalize the first letter of each word. By default, it uses the NLTK corpus of English words, but you can provide your own vocabulary list.

The function takes the following parameters:
- `no_words`: The number of words to include in the password.
- `separator`: The separator to use between the words (default is '--').
- `capitalization`: A boolean flag indicating whether to capitalize the first letter of each word.
- `vocabulary`: An optional list of words to choose from.

Example usage:
```python
memorable_password = generate_memorable_password(no_words=3, capitalization=True)
```

## PIN Password Generation
The `generate_pin_password` function generates a random PIN password consisting of a specified number of digits.

The function takes the following parameter:
- `length`: The length of the PIN password.

Example usage:
```python
pin_password = generate_pin_password(length=4)
```

Feel free to customize these functions according to your specific password requirements.

---
