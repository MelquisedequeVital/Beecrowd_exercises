i = 0
j = 1


while i <= 2:
    for n in range(3):
        if i != int(i):
            print(f"I={i:.1f} J={(j + n):.1f}")
        else:
            print(f"I={i:.0f} J={(j + n):.0f}")

    i = round(i + 0.2, 1)
    j = round(j + 0.2, 1)