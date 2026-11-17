import os

n, s = map(int, input().split())

for i in range(1, n + 1):
    with open(f"{i}.txt", 'a') as f:
        pass

while True:
    try:
        line = input()
        if (line == '\\end'):
            break
        if (line == ''):
            continue
        hsh = (ord(line[0]) % n) + 1
        str = f"{hsh}.txt"
        i = 1
        while os.path.exists(str):
            with(open(str, 'a+')) as f:
                f.seek(0)
                l = len(f.read().replace('\n', "")) + len(line)
            if l <= s:
                break
            str = f"{hsh}-{i}.txt"
            i = i + 1
        else:
            l = len(line)
        with open(str, 'a') as f:
            print(f"{l} characters in the file. At most {s-l} more chars to go")
            f.write(line + "\n")

        print(str)
    except (EOFError, KeyboardInterrupt):
        break

print("Program has ended")
