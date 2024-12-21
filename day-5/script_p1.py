data = open("input.txt", "r")
data  = data.read().split("\n")

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

sum = 0
for update in updates:
    correct = True
    for i in range(len(update)-1):
        incorrect = False
        for j in range(i+1, len(update)):
            check = update[i] + '|' + update[j]
            if (check not in rules):
                incorrect = True
                break
        if incorrect:
            correct = False
            break
    if correct:
        sum += int(update[int(len(update)/2)])

print(sum)