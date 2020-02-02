#def alphabet_position(val):
    #val = input("Put the sentence in: ")
 #   output = []
  #  for char in val:
   #     number = ord(char)
    #    if 97 <= number and number <= 122:
     #       number = number-96
      #      output += str(number)+' '
       # elif 65 <= number and number <= 90:
        #    number = number-64
         #   output += str(number)+' '
    #return " ".join(output).strip()

#print(alphabet_position("The sunset o'clock"))
    
def validate_pin(x):
    if len(x) != 4 and len(x) != 6:
        return False
    try:
        int(x)
        return True
    except:
        return False
