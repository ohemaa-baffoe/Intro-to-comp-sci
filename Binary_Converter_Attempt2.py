# STARTER CODE
# Create a variable to store the decimal number to be converted
dec = 116
# Print the first part of the answer 
# (end="" just means printed output continues on same line)
print(f"{dec} in binary is ", end="")
# Check place value 2^7
if (dec >= 128):
  print("1", end = "")
  dec -= 128
else:
  print("0", end = "")
# Continue for the rest of the place values from 2^6 down to 2^0




# leave this last line
print("")
