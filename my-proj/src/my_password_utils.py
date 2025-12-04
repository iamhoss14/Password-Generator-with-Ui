import random
import string
from abc import ABC, abstractmethod
import nltk


def ensure_nltk_words():
    """Ensure the NLTK 'words' corpus is downloaded. Idempotent and quiet."""
    try:
        from nltk.corpus import words as nltk_words
        # try to access to ensure the corpus is present
        _ = nltk_words.words()[:1]
    except LookupError:
        nltk.download('words', quiet=True)
    except Exception:
        # If something else goes wrong, don't crash the program here.
        pass


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        raise NotImplementedError()


class PinGenerator(PasswordGenerator):
    def __init__(self, length: int = 4):
        self.length = length

    def generate(self):
        return ''.join(random.choices(string.digits, k=self.length))


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 12, include_numbers: bool = True, include_symbols: bool = False):
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self):
        return ''.join(random.choices(self.characters, k=self.length))


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self, num_of_words: int = 4, separator: str = '-', capitalize: bool = False, vocabulary: list | None = None):
        if vocabulary is None:
            # try to use the nltk words corpus (sample a subset); fall back to a small list
            try:
                from nltk.corpus import words as nltk_words
                # take a filtered slice to avoid huge lists
                vocabulary = [w for w in nltk_words.words() if w.isalpha() and w.islower()][:1000]
            except Exception:
                vocabulary = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']

        self.vocabulary = vocabulary
        self.num_of_words = num_of_words
        self.separator = separator
        self.capitalize = capitalize

    def generate(self):
        password_words = [random.choice(self.vocabulary) for _ in range(self.num_of_words)]
        if self.capitalize:
            password_words = [word.capitalize() for word in password_words]
        return self.separator.join(password_words)


if __name__ == '__main__':
    ensure_nltk_words()
    print('Pin:', PinGenerator(8).generate())
    print('Random:', RandomPasswordGenerator(8, include_numbers=True, include_symbols=True).generate())
    print('Memorable:', MemorablePasswordGenerator(num_of_words=4, capitalize=True).generate())