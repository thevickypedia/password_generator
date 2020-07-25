import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = lower_case.upper()
numbers = '123456789'
punctuations = '!@#$%^&*()_+'

required_str = lower_case + upper_case + numbers + punctuations

key = "".join(random.choices(required_str, k=10))
print(key)
