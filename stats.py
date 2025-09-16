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

def dict_to_list(characters):
    new_list = []
    for character in characters:
        new_list.append({"char": character, "num": characters[character]})
    return new_list

def sort_on(items):
    return items["num"]

def sort_characters(characters):
    sorted_characters = dict_to_list(characters)
    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters

def get_report(sorted_characters):
    for character in sorted_characters:
        print(f"{character["char"]}: {character["num"]}")