print("Introduce two numbers.")
n = int(input())
m = int(input())
d = min(n, m)
for i in range (1, d+1):
    if n % i == 0 and m % i == 0:
        d = i
print(d)