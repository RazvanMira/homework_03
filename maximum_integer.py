import random
number = random.randint(1, 100)
print(number)
updates = 0
for i in range (1, 100):
    if number > i:
        pass
    else:
        number = i
        updates = updates +1
print(number)
print(updates)