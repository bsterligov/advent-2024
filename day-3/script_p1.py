data = open("input.txt", "r")

def check_start(element):
    if element[0] == "(":
          return True  
    return False

data  = data.read().split("mul")
data = list(filter(check_start, data))
sum = 0
for item in data:
    index = item.index(')') if ')' in item else -1
    if index != -1:
        sp = (item[1:index]).split(",")
        if (len(sp) == 2 and sp[0].isdigit() and sp[1].isdigit()):
            sum += int(sp[0]) * int(sp[1])

print(sum)