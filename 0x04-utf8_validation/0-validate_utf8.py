#!/usr/bin/python3
"""method that determines if a given data set represents
 a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle
the 8 least significant bits of each integer

"""


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Iterate through each byte in the data
    for byte in data:
        # Check if this byte is a start byte or a continuation byte
        if num_bytes == 0:
            if byte >> 7 == 0:
                # 1-byte character
                continue
            elif byte >> 5 == 0b110:
                # 2-byte character
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                # 3-byte character
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                # 4-byte character
                num_bytes = 3
            else:
                # Invalid start byte
                return False
        else:
            # Check if this byte is a continuation byte
            if byte >> 6 != 0b10:
                # Invalid continuation byte
                return False
            num_bytes -= 1

    # If there are remaining bytes, the data is invalid
    return num_bytes == 0
