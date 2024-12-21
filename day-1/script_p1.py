data = open("input.txt", "r")

left = []
right = []
for line in data.read().split("\n"):
    line = list(filter(None, line.split(" ")))
    if (len(line) == 0):
        continue
    left.append(line[0])
    right.append(line[1])

left.sort()
right.sort()

dist = 0
for i in range(len(left)):
    dist += abs(int(left[i]) - int(right[i]))

print(dist)