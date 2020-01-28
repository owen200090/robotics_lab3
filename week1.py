val = input("Put the sentence in: ")
val = val.lower()
output = []
for char in val:
    number = ord(char) - 96
    output.append(number)
    
print(output)
