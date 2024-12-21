data = open("input.txt", "r")

left = []
right = []

for line in data.read().split("\n"):
    line = list(filter(None, line.split(" ")))
    if len(line) == 0:
        continue
    left.append(line[0])
    right.append(line[1])

hash_map = {}

for item in right:
    if item not in hash_map:
        hash_map[item] = 1
    else:
        hash_map[item] += 1

dist = 0

for item in left:
    if item in hash_map:
        dist += hash_map[item] * int(item)

print(dist)
