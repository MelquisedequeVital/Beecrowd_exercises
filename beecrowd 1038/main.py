#Resolução com dicionário
id, qtd = list(map(int, input().split()))

itens = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50,

}

print(f'Total: R$ {(qtd*itens.get(id, 0.00)):.2f}')


#Resolução com if e else
"""if id == 1:
    total = 4.00 * qtd
elif id == 2:
    total = 4.50 * qtd
elif id == 3:
    total = 5.00 * qtd
elif id == 4:
    total = 2.00 * qtd
elif id == 5:
    total = 1.50 * qtd

print(f'Total: R$ {total:.2f}')"""