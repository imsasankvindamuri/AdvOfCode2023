file=open("./ProbFile1.txt",'r')
lst=(file.readlines())
direct={
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
    'zero':0
}
sum=0
lst2=[]
for string in lst:
    i=0
    while i<=len(string):
        if string[i:i+3]=='one' and i+3<=len(string):
            string=string[:i]+'1'+string[i+2:]
        elif string[i:i+3]=='two'and i+3<=len(string):
            string=string[:i]+'2'+string[i+2:]
        elif string[i:i+5]=='three'and i+5<=len(string):
            string=string[:i]+'3'+string[i+4:]
        elif string[i:i+4]=='four'and i+4<=len(string):
            string=string[:i]+'4'+string[i+3:]
        elif string[i:i+4]=='five'and i+4<=len(string):
            string=string[:i]+'5'+string[i+3:]
        elif string[i:i+3]=='six'and i+3<=len(string):
            string=string[:i]+'6'+string[i+2:]
        elif string[i:i+5]=='seven'and i+5<=len(string):
            string=string[:i]+'7'+string[i+4:]
        elif string[i:i+5]=='eight'and i+5<=len(string):
            string=string[:i]+'8'+string[i+4:]
        elif string[i:i+4]=='nine'and i+4<=len(string):
            string=string[:i]+'9'+string[i+3:]
        elif string[i:i+4]=='zero'and i+4<=len(string):
            string=string[:i]+'0'+string[i+3:]
        i+=1
    lst2.append(string)
lst=lst2
for string in lst:
    for i in string:
        try:
            dig1=int(i)
            break
        except ValueError:
            continue
    string=string[::-1]
    for i in string:
        try:
            dig2=int(i)
            break
        except ValueError:
            continue
    sum+=(10*dig1+dig2)
print(sum)