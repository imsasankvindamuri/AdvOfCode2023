import re
Max_Red = 12
Max_Blue = 14
Max_Green = 13

file = open("./ProbFile2.txt","r")
allGames = (file.readlines())
inver = 0
sum = 0
for i in allGames:
    set = i.split()
    ID = int(set[1][:-1])
    sum += ID
    set = set[2:]
    count = 0
    while count < len(set):
        color = set[count+1]
        if (bool(re.match(r'[a-zA-Z]$', color[-1]))==False):
            color=color[:-1]
        if (color == "blue"):
            if int(set[count]) > Max_Blue:
                inver += ID
                break
        if (color == "red"):
            if int(set[count]) > Max_Red:
                inver += ID
                break
        if (color == "green"):
            if int(set[count]) > Max_Green:
                inver += ID
                break
        count+=2
print(sum-inver)