def haming_distance(str1, str2):
    # comparing str1 with str2 so 64 bits of str1 will be compared to 16 bits of str1 16 bits at a time
    stra = str(str1)
    strb = str(str2)
    haming_dist = 0
    count = 0
    list1 = []
    if((len(stra) == 64)and (len(strb) == 16)):
        for i in range(0, 4, 1):
            for j in range(0, 16, 1):
                if stra[i*16+j] != strb[j]:
                    count += 1
            if(count < 8):
                return count
            list1.append(count)
            count = 0

        return min(list1)
    else:
        return False
