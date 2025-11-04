from typing import Callable
import sys


DICTIONARY: dict[str, str] = {}


def add_word() -> None:
    word = input("Word to add: ")
    meaning = input(f'Meaning of "{word}": ')
    DICTIONARY.update({word: meaning})
    print(f"{word} has been added to the dictionary!")


def get_word() -> None:
    word = input("Word to get: ")
    if word in DICTIONARY.keys():
        print(f'"{word}" means "{DICTIONARY[word]}"')
    else:
        print(f'"{word}" isn\'t in this dictionary :(')


def remove_word() -> None:
    word = input("Word to remove: ")
    if word in DICTIONARY.keys():
        DICTIONARY.pop(word)
        print(f'"{word}" has been successfully removed from the dictionary')
    else:
        print(f'"{word}" isn\'t in this dictionary :(')


def on_exit() -> None:
    print("Goodbye!")
    sys.exit(0)


MENU_OPTIONS: dict[int, tuple[str, Callable]] = {
    1: ("Get word", get_word),
    2: ("Add word", add_word),
    3: ("Delete word", remove_word),
    4: ("Exit", on_exit),
}


# val[0] refers to the name, val[1] the function that matches
MENU_TEXT = "\n".join([f"{i}: {val[0]}" for i, val in MENU_OPTIONS.items()]) + "\nEnter choice: "


def main() -> None:
    selections = {key: val[1] for key, val in MENU_OPTIONS.items()}
    while (choice := int(input(MENU_TEXT))):
        if choice not in MENU_OPTIONS.keys():
            continue
        selections[choice]()


if __name__ == '__main__':
    main()
