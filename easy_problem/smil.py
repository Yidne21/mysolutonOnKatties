inp = input()
for i in range(len(inp)):
    if inp[i] in ":;":
        if i != len(inp) - 1:
            if inp[i+1] == ")":
                print(i)
            elif inp[i+1] == "-" and inp[i+2] == ")":
                print(i)