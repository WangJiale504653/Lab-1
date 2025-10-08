for i in range(1,21):
    print("|",end="")
    if (21-i)%2==0:
        for j in range(1,(21-i)//2):
            print(" ",end="")
        print("\x1b[38;5;27m*\x1b[0m")
    else:
        print()

print("|",end="")
for k in range(1,20):
    print("_",end="")
