# (C * 9 / 5) + 32 = F
print("The following is a table that shows the conversion of temperature from Celsius to Fahrenheit.")
for C in range(0, 101, 10):
    F = (C * 9 / 5) + 32
    print(C , "degrees Celsius is equal to", F, "degrees Fahrenheit.")