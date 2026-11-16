n,s=map(int,input().split())

while True:
    try:
        line = input()
        print(line)
    except (EOFError, KeyboardInterrupt):
        break

print("Program has ended")
