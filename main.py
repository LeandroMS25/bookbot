import sys
from stats import get_number_of_words, get_number_of_each_character, sort_characters, get_report

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_book = sys.argv[1]
    text = get_book_text(path_book)
    num_words = get_number_of_words(text)
    num_of_each_character = get_number_of_each_character(text)
    sorted_characters = sort_characters(num_of_each_character) 
    print(f"Found {num_words} total words")
    get_report(sorted_characters)

main()
