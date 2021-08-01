from binascii import hexlify
from hashlib import sha1
from os import urandom
from uuid import uuid4, UUID


def generate_key() -> str:
    """Generates random alpha numeric key.

    Returns:
        str:
        Hexadecimal representation of the randomly generated alpha numeric value.
    """
    return hexlify(urandom(16)).decode()


def hashed(key: UUID) -> str:
    """Generates sha from UUID.

    Args:
        key: Takes the UUID generated as an argument.

    Returns:
        str:
        Hashed value of the UUID received.
    """
    return sha1(key.bytes + bytes(key.hex, "utf-8")).digest().hex()


if __name__ == '__main__':
    print(hashed(key=uuid4()))
