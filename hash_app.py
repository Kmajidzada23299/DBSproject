import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("n", type=int, help="number of buckets")
parser.add_argument("s", type=int, help="bucket size")
arguments = parser.parse_args()
n, s = arguments.n, arguments.s

def hash_func(input_string):
    hash_num = 0
    ln = len(input_string)

    for x in range(ln):
        hash_num += (ord(input_string[x]) * pow(31, ln - x - 1, n)) % n

    return hash_num % n


for i in range(1, n + 1):
    with open(f"{i}.txt", 'a') as f:
        pass

while True:

    try:
        line = input("Please enter the string:")

        if (line == ''):
            continue

        if (line[0] == "\\"):

            if (line == '\\end'):
                break

            elif (line == "\\d"):

                for file in os.listdir("."):

                    if file.endswith(".txt"):
                        print(file)

                continue

            elif (line == "\\getfile"):
                print(">", end=" ")

                try:
                    with open(input("file name:"), 'r') as f:
                        print("> "+ f.read())

                except FileNotFoundError:
                    print("file not found")
                    
                continue

            elif (line == "\\exists"):
                print("yes" if input("file name:") in os.listdir(".") else "no")
                continue

        if (len(line) > s):
            print("String cannot fit into bucket size that was allocated by second input at the start of the program")
            print("Restart the program with higher s parameter or use shorter text")
            continue

        hsh = hash_func(line) + 1
        string = f"{hsh}.txt"
        i = 0

        while os.path.exists(string):

            with(open(string, 'a+')) as f:
                f.seek(0)
                text = f.read()

                if ('\n' in text):
                    header = text.find('\n')
                    prev = string
                    string = text[:header]
                    i = i + 1
                    continue
            l = len(text) + len(line)

            if l <= s:
                break

            if (i == 0):
                string = f"{hsh}-1.txt"
                prev = f"{hsh}.txt"
            else:
                string = f"{hsh}-{i + 1}.txt"
                prev = f"{hsh}-{i}.txt"



        else:
            with open(prev, 'r+') as f:
                data = f.read()
                f.seek(0)
                f.write(string + '\n' + data)
                f.truncate()
            l = len(line)

        with open(string, 'a') as f:
            print(f"{l} characters in the file. {s - l} free slots remain")
            f.write(line)

        print(f"Text added to {string}")

    except (EOFError, KeyboardInterrupt):
        break

print("Program has ended")
