sum = 0
other_guest = True
while other_guest:
    age = input("Introduce the age of the guest, if no more guests enter blank line.\n")
    if age == "":
        other_guest = False
    else:
        age = int(age)
        if age <= 2:
            sum = sum + 0
        elif age > 2 and age <= 12:
            sum = sum + 14
        elif age > 12 and age < 65:
            sum = sum + 23
        elif age >= 65:
            sum = sum + 18
print("The admission cost for the group is $" + "{:.2f}".format(sum))