data = open("input.txt", "r")
data  = data.read().split("\n")

mas = "MAS"
sam = "SAM"
sum = 0
for i in range(1,len(data)-1):
    for j in range(1,len(data[i])-1):
        if data[i][j] == "A":
            diag = data[i-1][j-1] + data[i][j] + data[i+1][j+1]
            back_diag = data[i-1][j+1] + data[i][j] + data[i+1][j-1]
            if ((diag == mas or diag == sam) and (back_diag == mas or back_diag == sam)):
                sum += 1
print(sum)