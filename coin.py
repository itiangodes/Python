num = int(input("Enter amount: "))

ten = 0
five = 0
two = 0
one = 0

while (num!=0):
    if (num>= 10):
        num -= 10
        ten += 1
    elif (num>= 5):
        num -= 5
        five += 1
    elif (num>= 2):
        num -= 2
        two += 1
    elif (num>= 1):
        num -= 1
        one += 1

if (ten!=0):
    print ("Amount of Ten peso coin: ", ten)
if (five!=0):
    print ("Amount of five peso coin: ", five)
if (two!=0):
    print ("Amount of Two peso coin: ", two)
if (one!=0):
    print ("Amount of one peso coin: ", one)
