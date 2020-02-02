def alphabet_position(val):
    output = []
    for char in val:
        number = ord(char)
        if 97 <= number and number <= 122:
            number = number-96
            output += str(number)+' '
        elif 65 <= number and number <= 90:
            number = number-64
            output += str(number)+' '
    return " ".join(output).strip()

print(alphabet_position("The sunset o'clock"))
