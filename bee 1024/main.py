N = int(input())

for i in range(N):
    palavra = input()
    crip = ""
    invert = ""
    final = ""

    for letra in palavra:
        if letra.isalpha():
            crip += chr(ord(letra)+3)
        else:
            crip += letra

    for i in range(len(crip)-1, -1, -1):
        invert += crip[i]

    for i in range(len(invert)):
        if i < int(len(invert)/2):
            final += invert[i]
        else:
            final += chr(ord(invert[i])-1)


    print(final)