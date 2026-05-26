# simple_utils.py - A tiny utility library

def reverse_string(text):
    """Reverses the characters in a string."""
    # [::-1] returns the same string in reverse order.
    return text[::-1]


def count_words(sentence):
    # split() separates the sentence by whitespace; len() counts the words.
    return len(sentence.split())


def celsius_to_fahrenheit(celsius):
    # Converts Celsius to Fahrenheit using the standard formula.
    return (celsius * 9/5) + 32
