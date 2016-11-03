count = 1
tri_num = 1
i = 1
while count <= 500:
    count = 2
    for x in range(1,tri_num/2):
        if tri_num%x == 0:
            count = count + 1
#     if count >= 500:
    print tri_num, count
    i = i + 1
    tri_num = tri_num + i
    if count%50 == 0:
        print count, tri_num