import os
import random
import re
from binascii import hexlify, unhexlify
from itertools import zip_longest

string = "This is a sample string to be secured"


def deep_hex():
    return [
        '\\u00' + '\\u00'.join(re.findall('..?', str_to_hex)),
        '\\u00' + '\\u00'.join(map('{}{}'.format, *(str_to_hex[::2], str_to_hex[1::2]))),
        '\\u00' + '\\u00'.join(a + b for a, b in zip(str_to_hex[::2], str_to_hex[1::2])),
        '\\u00' + '\\u00'.join(str_to_hex[i:i + 2] for i in range(0, len(str_to_hex), 2)),
        '\\u00' + '\\u00'.join(f'{str_to_hex[i:i + 2]}' for i in range(0, len(str_to_hex), 2)),
        '\\u00' + '\\u00'.join([''.join(item) for item in zip(str_to_hex[::2], str_to_hex[1::2])]),
        '\\u00' + '\\u00'.join(a + b for a, b in zip_longest(str_to_hex[::2], str_to_hex[1::2], fillvalue="")),
        ''.join([f'\\u00{e}{str_to_hex[i + 1]}' for i, e in enumerate(str_to_hex) if i < len(str_to_hex) - 1][::2])
    ]


str_to_hex = hexlify(string.encode(encoding='utf-8')).decode(encoding='utf-8')
str_to_hex = random.choice(deep_hex()) if os.environ.get('DEEP_HEX') else str_to_hex
if str_to_hex.startswith('\\'):
    print("Processing as bytes")
    hex_to_str = bytes(str_to_hex, "utf-8").decode(encoding="unicode_escape")
else:
    print("Processing as hex")
    hex_to_str = unhexlify(str_to_hex).decode("utf-8")

assert hex_to_str == string
