
n = int(input("enter a number"))

sum = 0
tem = n

while tem > 0:
    digit = tem % 10
    sum += digit ** 3
    tem //= 10

if (n == sum) :
    print("it is a armstrrong number")

else :
    print("it is not a armstrong number")
