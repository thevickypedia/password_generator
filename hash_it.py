import time
import hashlib
from typing import Union, AnyStr


def hash_string(key: str) -> str:
    """Hash encodes a string into SHA512 and then hexifies it.

    Args:
        key: Key that has to be secured.

    Returns:
        str:
        Returns the hexified string.
    """
    encoded = key.encode('utf-8')
    signature = hashlib.sha512(encoded).hexdigest()
    return signature


def compare_digest(timestamp: Union[int, float], secret: str, hashed_val: AnyStr,
                   strict: bool = True, timeout: int = 300) -> bool:
    """Compares the encoded value to the actual password.

    Args:
        timestamp: Timestamp if included.
        secret: Plain text password to compare against.
        hashed_val: Hashed value to compare against.
        strict: Takes a boolean flag to compare only from the given timestamp and not before.
        timeout: Number of seconds before or after the time range has to be compared with.

    Returns:
        bool:
        Returns a boolean flag to indicate whether it's the right secret.
    """
    if strict:
        time_range = list(range(timestamp - 1, timestamp + timeout))
    else:
        time_range = list(range(timestamp - timeout, timestamp + timeout))
    for each in time_range:
        newly_hashed = hash_string(key=secret + str(each))
        if hashed_val == newly_hashed:
            print(f'Validated at {each}')
            return True
    else:
        print(f'{hashed_val!r} does not match')
        return False


if __name__ == '__main__':
    input_string = "This is a sample string to be secured"
    time_stamp = int(time.time())
    hashed = hash_string(key=input_string + str(time_stamp))
    print(hashed)
    compare_digest(timestamp=time_stamp, secret=input_string, hashed_val=hashed)
