from stats import init

def main():
    book_path = "books/frankenstein.txt"
    word_count, letter_list = init(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in letter_list:
        print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")

main()