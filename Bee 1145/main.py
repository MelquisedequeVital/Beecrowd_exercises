#Write an program that reads two numbers X and Y (X < Y). After this, show a sequence of 1 to y, passing to the next line to each X numbers.

X, Y = map(int, input().split())


for i in range(1, Y+1):
    print(i, end = [" ", "\n"][i%X == 0])




"""linha = 0

for i in range(Y):
    linha += 1
    if linha == X:
        print(f"{i + 1}", end = "\n")
        linha = 0
    else:
        print(f"{i + 1}", end = " ")"""