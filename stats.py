def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_number_of_each_character(text):
    number_of_character = {}
    words = text.lower().split()
    for word in words:
        for letter in word:
            if letter not in number_of_character:
                number_of_character[letter] = 0
            number_of_character[letter] += 1
    return number_of_character
