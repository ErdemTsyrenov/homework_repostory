"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""

from typing import List
from unicodedata import category
from collections import defaultdict


def read_chars(word, with_punctuation=True):
    chars = []
    is_unicode = False
    len_unicode = 0
    curr_uchar = ''
    for i in range(len(word)):
        if i != len(word)-1 and word[i] == '\\' and word[i+1] == 'u':
            is_unicode = True
            len_unicode = -1
        if is_unicode:
            if len_unicode >= 1 and len_unicode <= 3:
                curr_uchar += word[i]
            elif len_unicode == 4:
                curr_uchar += word[i]
                curr_uchar = chr(int(curr_uchar, base=16))
                if not with_punctuation:
                    if not category(curr_uchar).startswith('P'):
                        chars.append(curr_uchar)
                else:
                    chars.append(curr_uchar)
                curr_uchar = ''
                is_unicode = False
            len_unicode += 1
        elif not is_unicode:
            if not with_punctuation:
                if not category(word[i]).startswith('P'):
                    chars.append(word[i])
            else:
                chars.append(word[i])
    return chars


def is_unique(chars):
    if len(chars) == 0:
        return False
    return len(chars) == len(set(chars))


def get_longest_diverse_words(file_path: str) -> List[str]:
    unique_words = set()
    with open(file_path) as f:
        for line in f:
            words = line.split()
            for word in words:
                chars = read_chars(word, with_punctuation=False)
                if is_unique(chars):
                    unique_words.add(''.join(chars))
    unique_words = sorted(unique_words, key=lambda s: len(s))
    return unique_words[-10:]


def get_rarest_char(file_path: str) -> str:
    char_count = defaultdict(int)
    with open(file_path) as f:
        for line in f:
            chars = read_chars(line)
            for c in chars:
                char_count[c] += 1
    rarest = ' '
    for char in char_count:
        if char_count[char] < char_count[rarest]:
            rarest = char
    return rarest


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path) as f:
        punct_count = 0
        for line in f:
            chars = read_chars(line)
            for char in chars:
                if category(char).startswith('P'):
                    punct_count += 1
        print(punct_count)


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path) as f:
        non_ascii_count = 0
        for line in f:
            chars = read_chars(line)
            for char in chars:
                if ord(char) > 127:
                    non_ascii_count += 1
        print(non_ascii_count)


def get_most_common_non_ascii_char(file_path: str) -> str:
    non_ascii_char_count = defaultdict(int)
    with open(file_path) as f:
        for line in f:
            chars = read_chars(line)
            for c in chars:
                if ord(c) > 127:
                    non_ascii_char_count[c] += 1
    most_common = ''
    for char in non_ascii_char_count:
        if non_ascii_char_count[char] > \
           non_ascii_char_count.get(most_common, 0):
            most_common = char
    return most_common
