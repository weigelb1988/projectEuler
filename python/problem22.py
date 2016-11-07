# 
# 
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# 
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# 
# What is the total of all the name scores in the file?
import string

# init the lookup dictionary for alphabet value
alphaValue = dict(zip(string.ascii_uppercase, [ord(c) % 32 for c in string.ascii_uppercase]))
finalTotal = 0
with open('names.txt') as f:
    lines = f.readlines()
    betterLines = []
    for line in lines:  # loop over the lines
        for name in line.split(","):  # loop over each name
            # put in to a sortable list
            betterLines.append(name[1:len(name) - 1])  # removing the " from beginning and end of each name
    sortLines = sorted(betterLines)
    for x in range(0, len(sortLines)):  # loop over the sorted names
        sumLetters = 0  #  reset the sum for each name
        for letter in list(sortLines[x]):  # loop over the letters
            try:
                sumLetters = sumLetters + alphaValue[letter]
            except:
                pass
        nameTotal = (x + 1) * sumLetters  # add one to x when multiplying to account to adjust to count starting at 1
        finalTotal = finalTotal + nameTotal
        
print(finalTotal)
