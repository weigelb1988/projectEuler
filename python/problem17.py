sum = 0
lengths = {0:0,1:len("one"), 2:len("two"), 3:len("three"), 4:len("four"), 
           5:len('five'), 6:len('six'), 7:len('seven'), 8:len('eight'), 
           9:len('nine'), 10:len('ten'), 11:len('eleven'), 12:len('twelve'),
           13:len('thirteen'), 14:len('fourteen'), 15:len('fifteen'), 
           16:len('sixteen'), 17:len('seventeen'), 18:len('eighteen'),
           19:len('nineteen'), 20:len('twenty'), 30:len('thirty'), 40:len('forty'),
           50:len('fifty'), 60:len('sixty'), 70:len('seventy'), 80:len('eighty'),
           90:len('ninety')}


for x in range(1,1001):
    num_hundreds = 0 
    this_line = 0
    if x > 100 and x%100!=0 and x != 1000:
        this_line = this_line + 3 # adding in "and"
    if x >= 100 and x != 1000:
        this_line = this_line + 7 # adding in "hundred"
        num_hundreds = x//100
        this_line = this_line + lengths[num_hundreds]
    if x == 1000:
        this_line = this_line + 8 + lengths[1]# adding in "one thousand"
        sum = sum + this_line
        break;
    #x=534
    #tens = (543-(5*100)) == 43
    #num_tens = 43//10 == 4
    #num_ones = 43%10 = 3
    if x%100 > 20:
        tens = (x-(num_hundreds*100))
        num_tens = tens//10
        num_ones = tens%10
    
        word_tens = num_tens*10
        this_line = this_line + lengths[word_tens]
        this_line = this_line + lengths[num_ones]
    else:
        this_line = this_line + lengths[x%100]
    print(x, this_line)
    sum = sum + this_line
  
print(sum, 21124-sum)  