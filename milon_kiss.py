MENU_TEXT = """
1. Get word
2. Add word
3. Delete word
4. Exit

Enter choice:
"""


def add_word(dictionary: dict[str, str]) -> None:
    word = input("Word to add: ")
    meaning = input(f'Meaning of "{word}": ')
    dictionary.update({word: meaning})
    print(f"{word} has been added to the dictionary!")


def get_word(dictionary: dict[str, str]) -> None:
    word = input("Word to get: ")
    if word in dictionary.keys():
        print(f'"{word}" means "{dictionary[word]}"')
    else:
        print(f'"{word}" isn\'t in this dictionary :(')


def remove_word(dictionary: dict[str, str]) -> None:
    word = input("Word to remove: ")
    if word in dictionary.keys():
        dictionary.pop(word)
        print(f'"{word}" has been successfully removed from the dictionary')
    else:
        print(f'"{word}" isn\'t in this dictionary :(')


def main() -> None:
    dictionary: dict[str, str] = {}
    while (choice := int(input(MENU_TEXT))):
        if choice == 1:
            get_word(dictionary)
        if choice == 2:
            add_word(dictionary)
        if choice == 3:
            remove_word(dictionary)
        if choice == 4:
            print("goodbye!")
            break


if __name__ == '__main__':
    main()
