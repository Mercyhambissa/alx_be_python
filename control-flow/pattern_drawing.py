size = int(input("Enter the size of the pattern: "))
i = 0
while i < size:
    j = 0
    for j in range(size):
        print("*",end="")
        j += 1
    i += 1
    print()