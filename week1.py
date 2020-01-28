def alphabet_position(val):
    #val = input("Put the sentence in: ")
    val = val.lower()
    output = []
    for char in val:
        number = ord(char) - 96
        if number != -64:
            output.append(str(number))
    return " ".join(output)
    
