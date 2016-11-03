exp = 2**1000
strExp = str(exp)

listExp = list(strExp)
answer = 0
for x in range(0, len(listExp)):
    answer = answer + int(listExp[x])
    
print(answer)