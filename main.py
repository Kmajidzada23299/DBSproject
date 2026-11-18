import os
import argparse

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

            if (line=="\\d"):

                for file in os.listdir("."):

                    if file.endswith(".txt"):
                        print(file)

            if (line=="\\getfile"):
                print(">", end=" ")

                try:
                    with open(input("file name:"), 'r') as f:
                        print("> "+ f.read())

                except FileNotFoundError:
                    print("file not found")

            continue


        if (len(line) > s):
            print("String cannot fit into bucket size that was allocated by second input at the start of the program")
            print("Restart the program with higher s parameter or use shorter text")
            continue

        hsh = hash_func(line) + 1
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
