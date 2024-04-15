def decimal_to_hex(decimal_num):
    # Dictionary to map decimal digits to hexadecimal digits
    hex_map = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    # Initialize an empty string to store the hexadecimal representation
    hex_str = ""

    # Perform bit manipulation to convert decimal to hexadecimal
    while decimal_num > 0:
        # Extract the least significant 4 bits (hexadecimal digit) using bitwise AND with 0xF (binary: 1111)
        hex_digit = decimal_num & 0xF
        # Map the hexadecimal digit to its corresponding character
        hex_digit_char = hex_map.get(hex_digit, str(hex_digit))
        # Prepend the hexadecimal digit character to the result string
        hex_str = hex_digit_char + hex_str
        # Right shift the decimal number by 4 bits to discard the least significant 4 bits
        decimal_num >>= 4

    return hex_str


# Example usage
decimal_num = 305
print("Decimal:", decimal_num)
print("Hexadecimal:", decimal_to_hex(decimal_num))
