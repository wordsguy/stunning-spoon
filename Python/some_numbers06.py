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
        return ''.join(collection)

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
        return '| |'.join(random.choices(
            pool,
            k=length))
        # ''


def main():
    pool = get_collection(
        upper=False,
        lower=True,
        numbers=True,
        special=False)

    for w_list in generate_multiple(
        8,
        8,
        pool
    ):
        print(w_list)

         
        f = open("x.txt", "w")
        for w_list in generate_multiple(
        8,
        8,
        pool
    ):
            f.write(str(w_list) + "\n")
            f.close

if __name__ == '__main__':
    main()
