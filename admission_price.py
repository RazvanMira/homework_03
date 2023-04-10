print("The programme ends when you introduce a blank line.")
sum = 0
age = float(input("Introduce the age of the first guest.\n"))
while age != 0:
    if age <= 2:
        sum = sum + 0
    elif age > 2 and age <= 12:
        sum = sum + 14
    elif age > 12 and age < 65:
        sum = sum + 23
    elif age >= 65:
        sum = sum + 18
    age = float(input("Introduce the age of the next guest.\n"))
print("The admission cost for the group is $" + "{:.2f}".format(sum))