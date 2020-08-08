import os
import random
import string


def keygen():
    required_str = string.ascii_letters + string.digits + string.punctuation
    key = "".join(random.choices(required_str, k=10))
    return key


def check_file():
    key = keygen()
    pass_file = os.path.isfile('password.txt')
    if pass_file:
        file = open('password.txt', 'a')
        if key not in file:
            file.write(f'{key}\n')
            print(key)
            file.close()
        else:
            print('Duplicate password has been generated. Please retry.')
            exit(0)
    else:
        f = open('password.txt', 'a')
        f.write(f'{key}\n')
        print(key)
        f.close()


if __name__ == '__main__':
    check_file()
