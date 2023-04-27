def question2(string):
    vString = ''
    cString = ''
    for i in range(len(string)):
        if string[i] in 'a,e,i,o,u':
            vString = vString+string[i]
        else:
            cString = cString + string[i]
    return vString , cString