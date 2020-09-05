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
        file = open('password.txt', 'r')
        if key not in file:
            file = open('password.txt', 'a')
            file.write(f'{key}\n')
            file.close()
        else:
            print('Duplicate password has been generated. Please retry.')
            exit(0)
    else:
        file = open('password.txt', 'a')
        file.write(f'{key}\n')
        file.close()
    return key


if __name__ == '__main__':
    print(check_file())
