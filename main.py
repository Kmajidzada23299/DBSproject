n,s=map(int,input().split())

for i in range(1,n+1):
    with open(f"{i}.txt",'w') as f:
        pass

while True:
    try:
        line = input()
        if(line=='\\end'):
            break
        str = f"{(ord(line[0]) % n)+1}.txt"
        with(open(str, 'r')) as f:
            l=len(f.read())+len(line)
            print(l)
            if l > s:
                str=f"{(ord(line[0]) % n)+1}-1.txt"
                with open(str,'a') as f:
                    f.write(line)
            else:
                with open(str,'a') as f:
                    f.write(line)
            print(str)
    except (EOFError, KeyboardInterrupt):
        break

print("Program has ended")
