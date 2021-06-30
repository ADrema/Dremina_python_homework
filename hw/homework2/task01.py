"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import re
import unicodedata


def get_longest_diverse_words(file_path: str, k: int, encoding="utf-8") -> list:
    """
    Returns k longest words from file contain the largest amount of unique symbols
    :param file_path:
    :param k: words number to be returned
    :param encoding: encoding parameter to read from file
    :return: respective words list
    """
    unique_words_dict = dict()

    file_words = set(get_words_from_file(file_path, encoding))

    # reform into words dict, with key = 'word', value = word's symbols set
    for word in file_words:
        unique_words_dict[word] = set(word)
    # sort dict by value length and alphabet
    sorted_dict = sorted(unique_words_dict.items(), key=lambda x: (len(x[0]), x[0]))

    return [word[0] for word in sorted_dict[-k:]]


def get_rarest_char(file_path: str, encoding="utf8") -> str:
    """
    Returns the rarest char in the file, chars are sorted in alphabetical order
    """
    counts = {}
    with open(file_path, encoding=encoding) as file:
        for line in file:
            for symbol in line.lower():
                counts[symbol] = counts.get(symbol, 0) + 1
        counts = sorted(counts.items(), key=lambda item: (item[1], item[0]))

    return counts[0:][0][0]


def count_punctuation_chars(file_path: str, encoding="utf8") -> int:
    punctuation_counter = int()
    pattern = "^P.+"

    with open(file_path, encoding=encoding) as file:
        for line in file:
            punctuation_counter += sum(
                1 if re.match(pattern, unicodedata.category(symbol)) else 0
                for symbol in line
            )

    return punctuation_counter


def count_non_ascii_chars(file_path: str, encoding="utf8") -> int:
    non_ascii_count = int()

    with open(file_path, encoding=encoding) as file:
        for line in file:
            if line.isascii():
                continue
            non_ascii_count += sum(1 if ord(x) > 127 else 0 for x in line)

    return non_ascii_count


def get_most_common_non_ascii_char(file_path: str, encoding="utf-8") -> str:
    chars_stat = {}

    with open(file_path, encoding=encoding) as file:
        for line in file:
            if line.isascii():
                continue

            for symbol in line.lower():
                if ord(symbol) < 127:
                    continue
                chars_stat[symbol] = chars_stat.get(symbol, 0) + 1

    chars_stat = sorted(chars_stat.items(), key=lambda item: (item[1], item[0]))

    return chars_stat[-1:][0][0]


def get_words_from_file(file_path: str, encoding="utf-8") -> list:
    """
    The function reads words line by line and units '-' delimited words

    :param file_path: path to the file
    :param encoding: encoding settings
    :return: words list
    """
    word_to_unite = ""
    file_words = []
    punctuation_pattern = "^P.+"

    with open(file_path, encoding=encoding) as file:
        for line in file:
            # to unite end sting delimited words
            if bool(file_words):
                last_word = file_words[len(file_words) - 1]

                if last_word.endswith("-"):
                    word_to_unite = last_word[:-1]
                    file_words = file_words[:-1]

            for word in line.rstrip("\n").split(" "):
                # unite split word
                if len(word_to_unite) > 0:
                    word = word_to_unite + word
                    word_to_unite = ""

                if len(word) == 0 or (
                        len(word) == 1
                        and re.match(punctuation_pattern, unicodedata.category(word))
                ):
                    continue

                if re.match(
                        punctuation_pattern, unicodedata.category(word[-1])
                ) and not word.endswith("-"):
                    word = word[:-1]

                file_words.append(word.lower())
    return file_words
