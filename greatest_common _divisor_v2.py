print("Introduce two numbers.")
n = int(input())
m = int(input())
d = min(n, m)
while m % d != 0 or n % d != 0:
    d = d - 1
print(d)