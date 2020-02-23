def remove_common(string):
    common = open("1-1000.txt").read().split();
    common = common[:200]

    words = string.lower().split()
    words = [x for x in words if not x in common]
    print(words)
    return " ".join(words)



if __name__ == '__main__':
    f = 'This is a test to see if I can make a count dictionary. This is this because this is this.'
    print(f)
    f = remove_common(f)
    print(f)