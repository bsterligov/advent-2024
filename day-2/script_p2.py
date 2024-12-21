data = open("input.txt", "r")


def is_safe(line):
    p = int(line[0]) - int(line[1]) > 0
    for i in range(len(line) - 1):
        i1 = int(line[i])
        i2 = int(line[i + 1])
        diff = i1 - i2 > 0
        if (p != diff) or (i1 == i2) or (abs(i1 - i2) > 3):
            return False
    return True


safe = 0
data = data.read().split("\n")
for line in data:
    line = list(filter(None, line.split(" ")))
    if len(line) == 0:
        continue
    if is_safe(line):
        safe += 1
    else:
        for i in range(len(line)):
            reduce = line.copy()
            del reduce[i]
            if is_safe(reduce):
                safe += 1
                break

print(safe)
