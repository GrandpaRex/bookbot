def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def sort_on(dict):
    return dict["num"]

def number_of_characters(book_string):
    result = book_string.lower()
    letter_dictionary = {}
    dictionary_list = []
    for words in result:
        if words.isalpha():
            if words in letter_dictionary:
                new_value = letter_dictionary[words] + 1
                letter_dictionary[words] = new_value
            else:
                letter_dictionary[words] = 1
    for letter in letter_dictionary:
        dictionary_list.append({"char": letter, "num": letter_dictionary[letter]})
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list

def number_of_words(book_string):
    result = book_string.split()
    number_of_words = 0
    for words in result:
        number_of_words += 1
    return number_of_words

def init(file_path):
    result = get_book_text(file_path)
    word_count = number_of_words(result)
    letter_dictionary = number_of_characters(result)
    return word_count, letter_dictionary