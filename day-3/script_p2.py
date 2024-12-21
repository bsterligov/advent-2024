data = open("input.txt", "r")
data = data.read()
dont = "don't()"
do = "do()"


def check_start(element):
    if element[0] == "(":
        return True
    return False


def execute(data):
    mul = data.split("mul")
    sum = 0
    for item in mul:
        index = item.index(")") if ")" in item else -1
        if index != -1:
            sp = (item[1:index]).split(",")
            if len(sp) == 2 and sp[0].isdigit() and sp[1].isdigit():
                sum += int(sp[0]) * int(sp[1])
    return sum


sum = 0
left = 0
right = data.index(dont) if dont in data else len(data)

while right < len(data) and len(data) != 0:
    sum += execute(data[left:right])

    data = data[right + len(dont) : len(data)]
    left = data.index(do) if do in data else len(data)
    right = data.index(dont) if dont in data else len(data)

print(sum)
