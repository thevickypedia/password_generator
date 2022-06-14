from binascii import hexlify, unhexlify

string = "This is a sample string to be secured"

str_to_hex = hexlify(string.encode(encoding='utf-8'))
print(str_to_hex)

hex_to_str = unhexlify(str_to_hex)
print(hex_to_str)
