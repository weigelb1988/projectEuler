count = 0
longest = 0
for starting in range(1,1000000):
    x=starting
    count = 1
    while x != 1:
        if x%2 == 0:
            x = x/2
        else:
            x = (3*x) +1
        count = count + 1
#     print starting, count
    if count > longest:
        longest = count
        print starting, longest  
        
    