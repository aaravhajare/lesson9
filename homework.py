n = int(input("Enter a number: "))

if n > 999:
    o = n // 2
    binary = ""

    while o > 0:
        binary = str(o % 2) + binary  # Store remainder (LSB) at the beginning
        o //= 2  # Floor divide by 2

    print(binary)  # Print the binary representation
else:
    print("Number not applicable")
