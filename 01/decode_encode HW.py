byte_string = b'r\xc3\xa9sum\xc3\xa9'

byte_string_decode = byte_string.decode("utf-8")
print(byte_string_decode)

latin_byte_string = byte_string_decode.encode("Latin-1")
print(latin_byte_string)

decode_string = latin_byte_string.decode("Latin-1")
print(decode_string)