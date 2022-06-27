from binascii import hexlify, unhexlify

string = "This is a sample string to be secured"

str_to_hex = hexlify(string.encode(encoding='utf-8')).decode(encoding='utf-8')
str_to_hex = "".join([f"\\u00{e}{str_to_hex[i + 1]}" for i, e in enumerate(str_to_hex) if i < len(str_to_hex) - 1][::2])
if str_to_hex.startswith('\\'):
    hex_to_str = bytes(str_to_hex, "utf-8").decode(encoding="unicode_escape")
else:
    hex_to_str = unhexlify(str_to_hex)
assert hex_to_str == string
