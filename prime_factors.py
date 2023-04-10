number = int(input("Introduce an integer (2 or greater).\n"))
factor = 2
if number < 2:
    print("You did not introduce a valid number.")
else:
    print("The prime factors of", number, "are:")
while factor <= number:
    if number % factor == 0:
        print(factor, end="\n")
        number = number / factor
    else:
        factor = factor + 1