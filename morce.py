def binary(binstr):
    if not binstr or not all(bit in '01' for bit in binstr):
        return ""

    valid_codes = set(range(65, 91)) | set(range(97, 123)) | {32}
    result_chars = []

    for i in range(0, len(binstr) - 7, 8):
        byte = binstr[i:i + 8]
        char_code = int(byte, 2)

        if char_code in valid_codes:
            result_chars.append(chr(char_code))

    return ''.join(result_chars)