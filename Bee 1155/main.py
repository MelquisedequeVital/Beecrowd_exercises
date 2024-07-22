#Calculer o valor de S, sendo S = 1 + 1/2 + 1/3 + .... + 1/100

denominador = 1
somatorio = 0

while True:
    somatorio += 1/denominador
    denominador += 1
    if denominador == 101:
        break

print(f"{somatorio:.2f}")