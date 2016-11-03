import math
#shortest path formula = ((2n)!)/(n!)**2 
top = math.factorial(20*2)
bottom = math.factorial(20)**2

answer = top/bottom

print(answer)
