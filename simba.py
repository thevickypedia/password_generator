import string
import random


def keygen():
    required_str = string.ascii_letters + string.digits + string.punctuation
    key = "".join(random.choices(required_str, k=10))
    return key


if __name__ == '__main__':
    print(keygen())
