def solution2(A, B):
    # count = 0
    pairs = {}
    if len(A) == 0:
        return 0
    else:
        for i in range(len(A)):
            pairs[i + 1] = [A[i], B[i]]
        pairs2 = pairs.copy()
        for key in pairs:
            rangeA = pairs[key][0]
            rangeB = pairs[key][1]
            for key2 in pairs:
                if key2 == key:
                    continue
                else:
                    # overlap
                    if rangeA <= pairs[key2][0] and pairs[key2][0] <= rangeB:
                        if pairs[key2][1] > rangeB:
                            pairs[key][1] = pairs[key2][1]
                            rangeB = pairs[key][1]
                            if key2 in pairs2 and key in pairs2:
                                pairs2[key][1] = pairs2[key2][1]
                                del pairs2[key2]
                        else:
                            if key2 in pairs2 and key in pairs2:
                                del pairs2[key2]
                    # overlap
                    else:
                        if rangeA <= pairs[key2][1] and pairs[key2][1] <= rangeB:
                            if pairs[key2][0] < rangeA:
                                pairs[key][0] = pairs[key2][0]
                                rangeA = pairs[key][0]
                                if key2 in pairs2 and key in pairs2:
                                    pairs2[key][0] = pairs2[key2][0]
                                    del pairs2[key2]
                            else:
                                if key2 in pairs2 and key in pairs2:
                                    del pairs2[key2]
        return len(pairs2)
