print("Introduce the number of sides of the polygon.")
n = int(input())
if n == 0 or n == 1 or n == 2:
    print("A polygon must have at least three sides.")
    exit()
perimeter = 0
for length in range(1, n+1):
    length = float(input("Introduce the length of the side.\n"))
    perimeter = perimeter + length
print("The perimeter of the polygon is", perimeter)