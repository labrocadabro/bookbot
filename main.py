from pathlib import Path
from string import ascii_letters, ascii_lowercase
parent_folder = Path(__file__).parent
book_path = "books/frankenstein.txt"
book_location = parent_folder / book_path
with open(book_location) as f:
    contents = f.read()
    word_count = len(contents.split())
    letter_count = {}
    for letter in contents:
        letter = letter.lower()
        if letter in ascii_lowercase:
            if letter in letter_count.keys():
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for letter in sorted(letter_count.keys()):
        print(f"The letter '{letter}' appears {letter_count[letter]} times")
    print("The top 10 most frequently used letters are:")
    freq_sorted = sorted(letter_count.items(),
                         key=lambda x: x[1], reverse=True)
    for letter, count in freq_sorted[0:10]:
        print(f"{letter}: {count}")
    print("--- End report ---")
