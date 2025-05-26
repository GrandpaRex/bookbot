def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def number_of_characters(filepath):
    result = get_book_text(filepath).lower()
    letter_dictionary = {}
    for words in result:
        if words.isalpha():
            if words in letter_dictionary:
                new_value = letter_dictionary[words] + 1
                letter_dictionary[words] = new_value
            else:
                letter_dictionary[words] = 1
    return letter_dictionary