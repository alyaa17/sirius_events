c = 0
with open('text') as file:
    for line in file:
        for elem in line:
            c += 1



print(c // 2)
