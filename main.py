def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    char_dict = get_char_count(text)
    # print(f"There are {num_words} words in this document")
    # print(char_dict)
    report(text, char_dict, book_path, num_words)

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_dict = {}
    for letter in text:
        clean_letter = letter.lower()
        if clean_letter not in char_dict:
            char_dict[clean_letter] = 1
        else:
            char_dict[clean_letter] += 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def make_list(dict_to_convert):
    char_list = []
    for key, value in dict_to_convert.items():
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = value
        char_list.append(new_dict)
    return char_list

def report(text, character_count, path, num_words):
    char_list = make_list(character_count)
    char_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    for char_dict in char_list:
        if char_dict["char"].isalpha():
            print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()