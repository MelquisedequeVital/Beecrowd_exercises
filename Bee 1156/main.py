#Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula: S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?

numerador = 1
denominador = 1
somatorio = 0

while True:
    somatorio += numerador/denominador
    numerador += 2
    denominador *= 2
    if numerador > 39:
        break

print(f'{somatorio:.2f}')
