#Write a program that read two numbers X and Y and print the result of dividing the X by Y. If it's not possible, print the message "divisao impossivel".
N = int(input())

for i in range(N):
    X, Y = map(int, input().split())
    if Y == 0:
        print("divisao impossivel")
    else:
        resposta = X/Y
        print(f"{resposta:.1f}")
