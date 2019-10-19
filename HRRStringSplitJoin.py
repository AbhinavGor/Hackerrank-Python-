def split_and_join(line):
    words = line.split(" ")

    out = "-".join(words)

    return out
    # write your code here

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result