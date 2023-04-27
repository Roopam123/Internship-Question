def question1(li):
    minNum = li[0]
    maxNum = li[0]
    for i in range(len(li)):
        if li[i]>maxNum:
            maxNum = li[i]
        elif li[i]<minNum:
            minNum = li[i]
    return minNum, maxNum