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


def get_longest_various_symbols_words_from_file(
        file_path: str, quantity: int, encoding="utf-8"
) -> list:
    """
    Returns k longest words from file contain the largest amount of unique symbols
    :param file_path:
    :param quantity: words number to be returned
    :param encoding: encoding parameter to read from file
    :return: respective words list
    """
    unique_words_dict: dict[str, set] = dict()

    file_words = set(get_words_from_file(file_path, encoding))

    # reform into words dict, with key = 'word', value = word's symbols set
    for word in file_words:
        unique_words_dict[word] = set(word)
    # sort dict by value length and alphabet (x[0])
    sorted_list: list[str] = sorted(
        unique_words_dict.items(), key=lambda x: (len(x[0]), x[0])
    )

    return [word[0] for word in sorted_list[-quantity:]]


def get_rarest_char_from_file(file_path: str, encoding="utf8") -> str:
    """
    Returns the rarest char in the file, chars are sorted in alphabetical order
    """
    counts: dict[tuple[str:int]] = {}
    with open(file_path, encoding=encoding) as file:
        for line in file:
            for symbol in line.lower():
                counts[symbol] = counts.get(symbol, 0) + 1
        # sort dict by value and alphabet (x[0])
        counts: list[tuple[str, int]] = sorted(
            counts.items(), key=lambda item: (item[1], item[0])
        )
        print(counts)

    return counts[0][0]


def get_punctuation_chars_count(file_path: str, encoding="utf8") -> int:
    text = str()
    punctuation_regexp = "^P.+"
    punctuation_counter = int()

    with open(file_path, encoding=encoding) as file:
        text = "".join(file.readlines())

    punctuation_counter += sum(
        1 if re.match(punctuation_regexp, unicodedata.category(symbol)) else 0
        for symbol in text
    )

    return punctuation_counter


def get_non_ascii_chars_count(file_path: str, encoding="utf8") -> int:
    non_ascii_count = int()

    with open(file_path, encoding=encoding) as file:
        file_text: str = "".join(file.readlines())
        non_ascii_count += sum(1 if ord(x) > 127 else 0 for x in file_text)

    return non_ascii_count


def get_most_common_non_ascii_char_from_file(file_path: str, encoding="utf-8") -> str:
    chars_dict: dict[tuple[str:int]] = {}

    with open(file_path, encoding=encoding) as file:
        file_text: str = "".join(file.readlines())
        for symbol in file_text.lower():
            if ord(symbol) >= 127:
                chars_dict[symbol] = chars_dict.get(symbol, 0) + 1

    chars_list: list[tuple[str, int]] = sorted(
        chars_dict.items(), key=lambda item: (item[1], item[0])
    )

    return chars_list[-1:][0][0]


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
