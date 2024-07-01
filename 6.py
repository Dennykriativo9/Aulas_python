# 6)Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
#  A formula de conversão : F = C∗(9.0/5.0)+32:0, sendo F a temperatura em Fahrenheit
#   e C a temperatura em Celsius.


# Resolução 

# dados de entrada : o Valor da Temperatura
# dados de saida : o Valor da conversão

temperatura_celsius=float(input(" Porfavor Digite o Valor da Temperatura em Graus Celsius: "))
temperatura_fahre = float(temperatura_celsius*(9.0/5.0)+32.0)

print(f"{temperatura_celsius} Celsius equiva a {temperatura_fahre} Fahrenheit")