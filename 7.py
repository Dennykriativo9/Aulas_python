# 7)Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
#A formula de conversão e: C = 5.0 ∗ (F − 32.0)/9.0, sendo C a temperatura em Celsius
#e F a temperatura em Fahrenheit.

# dados de entrada : o Valor da Temperatura
# dados de saida : o Valor da conversão

temperatura_fahre=float(input(" Porfavor Digite o Valor da Temperatura em Graus Fahrenheit: "))
temperatura_celsius = float(5.0*(temperatura_fahre-32.0)/(9.0))

print(f"{temperatura_fahre} Fahrenheit equivale  a {temperatura_celsius} celsius")