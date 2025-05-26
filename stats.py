def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def number_of_words(filepath):
    result = get_book_text(filepath)
    split_result = result.split()
    number_of_words = 0
    for words in split_result:
        number_of_words += 1
    message = f"{number_of_words} words found in the document"
    return message