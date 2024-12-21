data = open("input.txt", "r")
data = data.read().split("\n")

rules = []
updates = []

is_rules = True
for line in data:
    if line == "":
        is_rules = False
        continue
    if is_rules:
        rules.append(line)
    else:
        updates.append(line.split(","))


def check_if_valid(update):
    for i in range(len(update) - 1):
        incorrect = False
        for j in range(i + 1, len(update)):
            check = update[i] + "|" + update[j]
            if check not in rules:
                return (i, j)
    return (-1, -1)


sum = 0

for update in updates:
    (i, j) = check_if_valid(update)
    if (i, j) == (-1, -1):
        continue
    while (i, j) != (-1, -1):
        (i, j) = check_if_valid(update)
        (update[i], update[j]) = (update[j], update[i])

    sum += int(update[int(len(update) / 2)])

print(sum)
