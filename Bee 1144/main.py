#Write a program that reads an integer N. N * 2 lines must be printed by this program according to the example below. For numbers with more than 6 digits, all digits must be printed (no cientific notation allowed).

#resolução youtube
N = int(input())


n1 = 1

for i in range(N*2):

    print(f"{n1} {n1**2 + (i%2)} {n1**3 + (i%2)}")
    n1 += (i%2)


"""N = int(input())
n = 1
c = 0

for i in range(N*2):
    if c == 0 :
        print(n, n**2, n**3)
    elif c % 2 == 0:
        print(n, n**2, n**3)
    else:
        print(n, n**2 + 1, n**3 + 1)
        n += 1

    c += 1"""
