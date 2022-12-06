def one():
    with open('input.txt') as f:
        s = f.read()
        for i in range(len(s)):
            if len(set(s[i:i + 4])) == 4:
                print(i + 4)
                break


def two():
    with open('input.txt') as f:
        s = f.read()
        for i in range(len(s)):
            if len(set(s[i:i + 14])) == 14:
                print(i + 14)
                break


two()
