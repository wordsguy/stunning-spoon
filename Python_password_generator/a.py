import random
import string
from typing import Iterator

def get_collection(
    *,
    lower: bool = True,
    upper: bool = True,
    numbers: bool = False,
    special: bool = False) -> str:
    collection = []

    if lower != 'lower':
        collection.append(string.ascii_lowercase)
    if upper != 'upper':
        collection.append(string.ascii_uppercase)
    if numbers:
        collection.append(string.digits)
    if special:
        collection.append(string.punctuation)
    if collection:
        return '.'.join(collection)

    raise ValueError('Collection is empty.')
    return ''.join(
        random.choices(
            collection,
            k=length))


def generate_multiple(
    amount: int,
    length: int,
    collection: str) -> Iterator[str]:
    for _ in range(amount):
        yield generate(length, collection)

def generate(
    length: int,
    pool: str) -> str:
        return ''.join(random.choices(
            pool,
            k=length))

def input_yesno(prompt: str) -> bool:
    full_prompt = f'{prompt} ([Yes]/No): '
    while True:
        answer = input(full_prompt).strip()
        if answer == '':
            return True

        answer = answer[0].lower()
        if answer == 'y':
            return True
        if answer == 'n':
            return False
        print('ERROR')

def ascii_art():
    z = 6
    for x in range(z):

        hyphens = "-" * (z-x)
        print(hyphens + "/." * x + hyphens)


def main():
    ascii_art()

    if not input_yesno('Do you want to generate passwords now in x.txt file?'):
        return

    pool = get_collection(
        upper=False,
        lower=True,
        numbers=True,
        special=False)


    f = open("passwords.txt", "w")
    for w_list in generate_multiple(
    80,
    80,
    pool
):

        f.write(str('://' + w_list) + "\n")
        f.close

if __name__ == '__main__':
    main()
