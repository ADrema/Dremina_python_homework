import pytest

from hw.homework2.task01 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)

one_line_file_path = "../common_files/test_data_one_line.txt"
data_file_path = "../common_files/data.txt"
encoding = "unicode_escape"

non_ascii_chars_data_provider = [(one_line_file_path, 1), (data_file_path, 2972)]


@pytest.mark.parametrize("filepath, expected", non_ascii_chars_data_provider)
def test_non_ascii_chars_counter_function(filepath, expected):
    assert count_non_ascii_chars(filepath, encoding=encoding) == expected


punctuation_counter_data_provider = [(one_line_file_path, 2), (data_file_path, 5475)]


@pytest.mark.parametrize("filepath, expected", punctuation_counter_data_provider)
def test_punctuation_chars_function(filepath, expected):
    assert count_punctuation_chars(filepath, encoding=encoding) == expected


rarest_char_data_provider = [(one_line_file_path, ","), (data_file_path, "(")]


@pytest.mark.parametrize("filepath, expected", rarest_char_data_provider)
def test_rarest_char_function(filepath, expected):
    assert get_rarest_char(filepath, encoding=encoding) == expected


most_common_non_ascii_data_provider = [(one_line_file_path, "—"), (data_file_path, "ä")]


@pytest.mark.parametrize("filepath, expected", most_common_non_ascii_data_provider)
def test_most_common_non_ascii_function(filepath, expected):
    assert get_most_common_non_ascii_char(filepath, encoding=encoding) == expected


longest_diverse_words_data_provider = [
    (one_line_file_path, 2, ["idylle", "waldgang"]),
    (
        data_file_path,
        10,
        [
            "politisch-technischen",
            "résistance-bewegungen",
            "werkstättenlandschaft",
            "mehrheitsvorstellungen",
            "souveränitätsansprüche",
            "symbolischsakramentale",
            "wiederbelebungsübungen",
            "zoologisch-politischen",
            "politisch-strategischen",
            "verfassungsverletzungen",
        ],
    ),
]


@pytest.mark.parametrize(
    "filepath, words_number, expected", longest_diverse_words_data_provider
)
def test_get_longest_diverse_words(filepath, words_number, expected):
    assert (
            get_longest_diverse_words(filepath, words_number, encoding=encoding) == expected
    )
