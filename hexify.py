import base64
import binascii
import re
import string
from itertools import zip_longest

input_string = "This is a sample string to be secured"

UNICODE_PREFIX = base64.b64decode(b'XA==').decode(encoding="ascii") + string.ascii_letters[20] + string.digits[:1] * 2


def deep_hex(hexed):
    return [
        UNICODE_PREFIX + UNICODE_PREFIX.join(re.findall('..?', hexed)),
        UNICODE_PREFIX + UNICODE_PREFIX.join(map('{}{}'.format, *(hexed[::2], hexed[1::2]))),
        UNICODE_PREFIX + UNICODE_PREFIX.join(a + b for a, b in zip(hexed[::2], hexed[1::2])),
        UNICODE_PREFIX + UNICODE_PREFIX.join(hexed[i:i + 2] for i in range(0, len(hexed), 2)),
        UNICODE_PREFIX + UNICODE_PREFIX.join(f'{hexed[i:i + 2]}' for i in range(0, len(hexed), 2)),
        UNICODE_PREFIX + UNICODE_PREFIX.join([''.join(item) for item in zip(hexed[::2], hexed[1::2])]),
        UNICODE_PREFIX + UNICODE_PREFIX.join(a + b for a, b in zip_longest(hexed[::2], hexed[1::2],
                                                                           fillvalue="")),
        UNICODE_PREFIX + UNICODE_PREFIX.join([e + hexed[i + 1] for i, e in enumerate(hexed)
                                              if i < len(hexed) - 1][::2]),
    ]


def hexlify():
    str_to_hex = binascii.hexlify(input_string.encode(encoding='utf-8')).decode(encoding='utf-8')
    for each in deep_hex(hexed=str_to_hex):
        if each.startswith('\\'):
            print("Processing as bytes")
            hex_to_str = bytes(each, "utf-8").decode(encoding="unicode_escape")
        else:
            print("Processing as hex")
            hex_to_str = binascii.unhexlify(each).decode("utf-8")
        assert hex_to_str == input_string


if __name__ == '__main__':
    hexlify()
