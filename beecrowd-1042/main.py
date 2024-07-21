valores = list(map(int, input().split()))

valores_copia =  valores.copy()
valores_copia.sort()

for valor in valores_copia:
    print(valor)

print("")

for valor in valores:
    print(valor)

    
"""for valor in sorted(valores):
    print(valor)

print("")

for valor in valores:
    print(valor)"""