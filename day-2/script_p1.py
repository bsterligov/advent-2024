data = open("input.txt", "r")

safe = 0
data = data.read().split("\n")
for line in data:
    line = list(filter(None, line.split(" ")))
    if len(line) == 0:
        continue
    is_safe = True
    p = int(line[0]) - int(line[1]) > 0
    for i in range(len(line) - 1):
        i1 = int(line[i])
        i2 = int(line[i + 1])
        diff = i1 - i2 > 0
        if (p != diff) or (i1 == i2) or (abs(i1 - i2) > 3):
            is_safe = False
            break
    if is_safe:
        safe += 1

print(safe)
