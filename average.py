import sys
print("To stop entering values press 0.")
print("Enter the values.")
sum = 0
counter = 0
average = 0
i = int(input())
if i == 0:
    print("Error, the first value can not be 0.")
    sys.exit()
while i != 0:
    sum = sum + i
    counter = counter + 1
    i = int(input("Introduce the next value.\n"))
average = sum / counter
print("The average of the values is", average)