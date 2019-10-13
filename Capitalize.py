def solve(string):
    i = 0
    result = list()
    temp = ""
    while i < len(string):
        if i == 0 and ord(string[i]) >= 97 and ord(string[i]) <= 122:
            x = ord(s[i]) - 32
            x = chr(x)
            result.append(x)
        elif (string[i - 1] == " ") and (string[i] != " ") and (ord(string[i]) >= 97) and (ord(string[i]) <= 122):
            x = ord(string[i]) - 32
            x = chr(x)
            nl.append(x)
        else:
            nl.append(string[i])
        i += 1
    for x in nl:
        temp = temp + x
    print(temp)


string = str(input())

solve(string)