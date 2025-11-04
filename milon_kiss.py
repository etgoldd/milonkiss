from typing import Callable
import sys


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

    menu_options: dict[int, tuple[str, Callable]] = {
        1: ("Get word", get_word),
        2: ("Add word", add_word),
        3: ("Delete word", remove_word),
    }
    selections: dict[int, Callable] = {key: val[1] for key, val in menu_options.items()}
    # val[0] refers to the name, val[1] the function that matches
    menu_text = "0: Exit\n"
    menu_text += "\n".join([f"{i}: {val[0]}" for i, val in menu_options.items()])
    menu_text += "\nEnter choice: "

    while (choice := int(input(menu_text))):
        if choice == 0:
            print("Goodbye!")
            break
        if choice not in menu_options.keys():
            continue
        selections[choice](dictionary)


if __name__ == '__main__':
    main()
