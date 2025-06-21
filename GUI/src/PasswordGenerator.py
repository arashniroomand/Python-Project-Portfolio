import random
import string
from abc import ABC, abstractmethod



class PasswordGenerator(ABC):
    """
    Abstract base class for password generators.
    """

    @abstractmethod
    def generator(self):
        """
        Abstract method to generate a password.
        """
        pass


class PinGenerator(PasswordGenerator):
    """
    A password generator that generates PIN passwords consisting of random digits.
    """

    def __init__(self, length: int):
        """
        Initialize the PinGenerator with the desired length of the PIN password.
        :param length: The length of the PIN password.
        """
        self.length = length

    def generator(self):
        """
        Generate a PIN password consisting of random digits.
        :return: The generated PIN password.
        """
        return ''.join([random.choice(string.digits) for _ in range(self.length)])


class RandomPasswordGenerator(PasswordGenerator):
    """
    A password generator that generates random passwords consisting of random characters, including letters, numbers, and symbols.
    """

    def __init__(self, length: int = 8, include_numbers=False, include_symbols=False):
        """
        Initialize the RandomPasswordGenerator with the desired length and options.
        :param length: The length of the random password.
        :param include_numbers: Whether to include numbers in the random password.
        :param include_symbols: Whether to include symbols in the random password.
        """
        self.length = length
        self.include_numbers = include_numbers
        self.include_symbols = include_symbols
        self.characters = string.ascii_letters
        if self.include_numbers:
            self.characters += string.digits
        if self.include_symbols:
            self.characters += string.punctuation

    def generator(self):
        """
        Generate a random password consisting of random characters.
        :return: The generated random password.
        """
        return ''.join([random.choice(self.characters) for _ in range(self.length)])


class MemorablePassword(PasswordGenerator):
    """
    A password generator that generates memorable passwords using a combination of random words from the English language.
    """

    def __init__(
            self,
            num_of_words,
            spectator='_',
            upper_case=True,
            vocabulary= ['amir','arash','moein','aghigh']
    ):
        """
        Initialize the MemorablePassword generator with the desired options.
        :param num_of_words: The number of words in the memorable password.
        :param spectator: The spectator character to separate words in the password.
        :param upper_case: Whether to use uppercase letters in the password.
        :param vocabulary: The vocabulary to use for generating words. If None, the NLTK words corpus is used.
        """
        
        
        self.vocabulary = vocabulary
        self.num_of_words = num_of_words
        self.spectator = spectator
        self.upper_case = upper_case

    def generator(self):
        """
        Generate a memorable password using a combination of random words.
        :return: The generated memorable password.
        """
        temp = ''
        for _ in range(self.num_of_words):
            chance = random.choice([True, False])
            if chance:
                temp += random.choice(self.vocabulary).upper() + self.spectator
            else:
                temp += random.choice(self.vocabulary).lower() + self.spectator

        password = temp[:-1]
        return password


def menu():
    """
    Display a menu and handle user input to generate passwords using the available options.
    """
    while True:
        print("Choose the type of password you want to generate:")
        print("1. PIN password")
        print("2. Random password")
        print("3. Memorable password")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            length = int(input("Enter the length of the PIN password: "))
            pin_generator = PinGenerator(length)
            print("Generated PIN password:", pin_generator.generator())
        elif choice == "2":
            length = int(input("Enter the length of the random password: "))
            include_numbers = input("Include numbers? (y/n): ").lower() == "y"
            include_symbols = input("Include symbols? (y/n): ").lower() == "y"
            random_password_generator = RandomPasswordGenerator(length, include_numbers, include_symbols)
            print("Generated random password:", random_password_generator.generator())
        elif choice == "3":
            num_of_words = int(input("Enter the number of words in the memorable password: "))
            spectator = input("Enter the spectator character: ")
            upper_case = input("Use uppercase letters? (y/n): ").lower() == "y"
            memorable_password = MemorablePassword(num_of_words, spectator, upper_case)
            print("Generated memorable password:", memorable_password.generator())
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
