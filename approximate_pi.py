pi = 3
mid_term = 2
for i in range(1, 16):
    if i % 2 == 1:
        pi = pi + (4 / (mid_term * (mid_term + 1) * (mid_term + 2)))
    else:
        pi = pi - (4 / (mid_term * (mid_term + 1) * (mid_term + 2)))
    mid_term = mid_term + 2
    print(pi)