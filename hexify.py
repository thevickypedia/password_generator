import base64
import binascii
import string

input_string = "This is a sample string to be secured"

UNICODE_PREFIX = base64.b64decode(b'XA==').decode(encoding="ascii") + string.ascii_letters[20] + string.digits[:1] * 2


def hexlify():
    str_to_hex = UNICODE_PREFIX + UNICODE_PREFIX.join(binascii.hexlify(data=input_string.encode(encoding="utf-8"),
                                                                       sep="-").decode(encoding="utf-8").split(sep="-"))
    hex_to_str = bytes(str_to_hex, "utf-8").decode(encoding="unicode_escape")
    assert hex_to_str == input_string


if __name__ == '__main__':
    hexlify()
