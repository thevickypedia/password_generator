import string
import random

required_str = string.ascii_letters + string.digits + string.punctuation

for a in range(8):
    key = "".join(random.choice(required_str))
    print(key)
