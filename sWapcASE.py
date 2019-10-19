def swap_case(s):
    alpha = list()
    for i in s:
        alpha.append(i)

    alphan = list()
    alphanew = list()
    alphaf = list()

    for i in alpha:
        alphan.append(ord(i))

    for i in alphan:
        if 96 < i < 123:
            i = i - 32
            alphanew.append(i)
        elif 64 < i < 91:
            i = i + 32
            alphanew.append(i)
        elif 31 < 48:
            i = i
            alphanew.append(i)

    for i in alphanew:
        alphaf.append(chr(i))
    #print(alphan)
    #print(alphanew)
    osting = ""

    for i in alphaf:
        osting = osting + i

    return osting


s = str(input(""))

print( swap_case(s))