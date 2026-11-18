import os

n, s = map(int, input().split())


def hashfunc(string):
    hsh = 0
    l = len(string)

    for x in range(l):
        hsh += ord(string[x]) * pow(31, l - x - 1) % n

    return hsh % n


for i in range(1, n + 1):
    with open(f"{i}.txt", 'a') as f:
        pass

while True:

    try:
        line = input("Please enter the string:")

        if (line == '\\end'):
            break

        if (line == ''):
            continue

        if (len(line) > s):
            print("String cannot fit into bucket size that was allocated by second input at the start of the program")
            print("Restart the program with higher s parameter or use shorter text")
            continue

        hsh = hashfunc(line) + 1
        string = f"{hsh}.txt"
        i = 1

        while os.path.exists(string):

            with(open(string, 'a+')) as f:
                f.seek(0)
                l = len(f.read()) + len(line)

            if l <= s:
                break

            string = f"{hsh}-{i}.txt"
            i = i + 1

        else:
            l = len(line)

        with open(string, 'a') as f:
            print(f"{l} characters in the file. {s - l} free slots remain")
            f.write(line)

        print(f"Test added to {string}")

    except (EOFError, KeyboardInterrupt):
        break

print("Program has ended")
