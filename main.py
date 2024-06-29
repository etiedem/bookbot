#!/usr/bin/env python3


from collections import Counter
from operator import itemgetter


def get_words(text):
    return len(text.split())


def char_counter(text):
    return Counter(x.lower() for x in text if x.isalpha())


def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()

    print(f"--- Begin report of {book} ---")
    print(f"{get_words(file_contents)} words found in document")
    print()
    for k, v in sorted(
        char_counter(file_contents).items(), key=itemgetter(1), reverse=True
    ):
        print(f"The '{k}' character was found {v:,} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
