from stats import get_number_of_words, get_number_of_each_character

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_number_of_words(text)
    num_of_each_character = get_number_of_each_character(text)
    print(f"{num_words} words found in the document")
    print(num_of_each_character)

main()
