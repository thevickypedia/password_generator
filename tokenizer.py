import binascii
import hashlib
import os
import uuid


def generate_key() -> str:
    """Generates random alpha numeric key.

    Returns:
        str:
        Hexadecimal representation of the randomly generated alpha numeric value.
    """
    return binascii.hexlify(os.urandom(16)).decode()


def hashed(key: uuid.UUID) -> str:
    """Generates sha from UUID.

    Args:
        key: Takes the UUID generated as an argument.

    Returns:
        str:
        Hashed value of the UUID received.
    """
    return hashlib.sha1(key.bytes + bytes(key.hex, "utf-8")).digest().hex()


if __name__ == '__main__':
    print(hashed(key=uuid.uuid4()))
