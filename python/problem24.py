
# function to swap array elements 
fullList = []
count = 0
def swap (v=[], i=0, j=0):
    t=0 

    t = v[i]
    v[i] = v[j]
    v[j] = t

# recursive function to generate permutations
def perm (v=[], n=0, i=0):

    # this function generates the permutations of the array
    # from element i to element n-1
    #
    j=0

#     if we are at the end of the array, we have one permutation
#     we can use (here we print it; you could as easily hand the
#     array off to some other function that uses it for something

    if i == n:
        num = ''
        for j in range(0,n):
            num = num + str(v[j])
#             print(v[j], end="")
#         print("\n" + num)
        fullList.append(int(num))
        
    else:
#         recursively explore the permutations starting
#         at index i going through index n-1
        for j in range(i,n):
#           try the array with i and j switched 

            swap (v, i, j);
            perm (v, n, i+1);

#           swap them back the way they were

            swap (v, i, j);
            
# little driver function to print perms of first 5 integers

PERM_NUM = 10
v = [];
for i in range(0,PERM_NUM):
     v.append(i)
perm(v, PERM_NUM, 0);
fullList.sort()
print("FULLLIST[999999]: " + str(fullList[999999]) + "FULLIST[1000000]: " + str(fullList[1000000]))
