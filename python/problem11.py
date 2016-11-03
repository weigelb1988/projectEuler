import math
w, h = 20, 20 
problem11String = [[0 for x in range(w)] for y in range(h)] 
problem11String[0] = [8, 02, 22, 97, 38, 15, 00, 40, 00, 75, 04, 05, 07, 78, 52, 12, 50, 77, 91, 8]
problem11String[1] = [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 04, 56, 62, 00]
problem11String[2] = [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 03, 49, 13, 36, 65]
problem11String[3] = [52, 70, 95, 23, 04, 60, 11, 42, 69, 24, 68, 56, 01, 32, 56, 71, 37, 02, 36, 91]
problem11String[4] = [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80]
problem11String[5] = [24, 47, 32, 60, 99, 03, 45, 02, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50]
problem11String[6] = [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70]
problem11String[7] = [67, 26, 20, 68, 02, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21]
problem11String[8] = [24, 55, 58, 05, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72]
problem11String[9] = [21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95]
problem11String[10] = [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 03, 80, 04, 62, 16, 14, 9, 53, 56, 92]
problem11String[11] = [16, 39, 05, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57]
problem11String[12] = [86, 56, 00, 48, 35, 71, 89, 07, 05, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58]
problem11String[13] = [19, 80, 81, 68, 05, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 04, 89, 55, 40]
problem11String[14] = [04, 52, 8, 83, 97, 35, 99, 16, 07, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66]
problem11String[15] = [88, 36, 68, 87, 57, 62, 20, 72, 03, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69]
problem11String[16] = [04, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36]
problem11String[17] = [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 04, 36, 16]
problem11String[18] = [20, 73, 35, 29, 78, 31, 90, 01, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 05, 54]
problem11String[19] = [01, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 01, 89, 19, 67, 48]

def is_square(apositiveint):
    x = apositiveint / 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint / x)) / 2
        if x in seen: return False
        seen.add(x)
    return True

def is_prime(pos_int):
    if pos_int == 1:
        return False
    if pos_int == 2:
        return True
    for x in range(2, pos_int):
        if pos_int % x == 0:
            return False
    return True

def is_naive_prime(pos_int):
    i = 5
    if pos_int <= 1:
        return False
    elif pos_int <= 3:
        return True
    elif (pos_int % 2 == 0) or (pos_int % 3 == 0):
        return False
    
    while (i * i) <= pos_int:
        if(pos_int % i == 0) or (pos_int % (i + 2) == 0):
            return False
        i = i + 6
    return True
total = 0
prevHigh = 0
for i in range(0, 20):
    for j in range(0, 16):
      
        up = 1
        down = 1
        left = 1
        right = 1
        diag_down = 1
        diag_up = 1
        try:
            print "DOWN: ",
            for x in range(0,4):
                down = down * problem11String[j+x][i]
                print problem11String[j+x][i],
        except OverflowError, MemoryError:
            traeback.print_exc()
        except:
            pass
        print "=",down
        if down > prevHigh:
            prevHigh = down
        try:
            print "RIGHT: ", 
            for x in range(0,4):
                right = right * problem11String[i][j+x]
                print problem11String[i][j+x],
            
                
                #66*70*54*59
        except OverflowError, MemoryError:
            traeback.print_exc()
        except:
            pass 
        print "=", right
        if right > prevHigh:
            prevHigh = right
for i in range(0, 16):
    for j in range(0, 16):
        diag_down = 1
        try:
            print "D_DOWN: ",
            for x in range(0,4):
                diag_down = diag_down * problem11String[i+x][j+x]
                #66*66*89*33
                print problem11String[i+x][j+x],
            
        except OverflowError, MemoryError:
            traeback.print_exc()        
        except:
            pass
        print "=",diag_down
        if diag_down > prevHigh:
            prevHigh = diag_down
        print"\n\n"
for i in range(3, 20):
    for j in range(0, 16):
        diag_down = 1
        try:
            print "D_DOWN: ",
            for x in range(0,4):
                diag_down = diag_down * problem11String[i+x][j-x]
                #66*66*89*33
                print problem11String[i+x][j-x],
            
        except OverflowError, MemoryError:
            traeback.print_exc()        
        except:
            pass
        print "=",diag_down, i , j
        if diag_down > prevHigh:
            prevHigh = diag_down
        print"\n\n"

print prevHigh
