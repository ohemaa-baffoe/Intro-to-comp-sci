# STARTER CODE
# Create a variable to store the decimal number to be converted
dec = 116
# Print the first part of the answer 
# (end="" just means printed output continues on same line)
print(f"{dec} in binary is ", end="")
# Check place value 2^7if (dec >= 128):
if dec >= 128:
    print("1", end="")
    dec -= 128
else:
    print("0", end="")

if dec >= 64:
    print("1", end="")
    dec -= 64
else:
    print("0", end="")

if dec >= 32:
    print("1", end="")
    dec -= 32
else:
    print("0", end="")

if dec >= 16:
    print("1", end="")
    dec -= 16
else:
    print("0", end="")

if dec >= 8:
    print("1", end="")
    dec -= 8
else:
    print("0", end="")

if dec >= 4:
    print("1", end="")
    dec -= 4
else:
    print("0", end="")

if dec >= 1:
    print("1", end="")
    dec -= 1
else:
    print("0", end="")

# Continue for the rest of the place values from 2^6 down to 2^0




# leave this last line
print("")
