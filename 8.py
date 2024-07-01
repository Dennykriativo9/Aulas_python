# 8)Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A
  #formula de conversão: C = K − 273.15, sendo C a temperatura em Celsius e K a
  #temperatura em Kelvin

# dados de entrada : o Valor da Temperatura
# dados de saida : o Valor da conversão

temperatura_kelvin=float(input(" Porfavor Digite o Valor da Temperatura em Graus Kelvin: "))
temperatura_celsius = float(temperatura_kelvin-273.15)

print(f"{temperatura_kelvin} Kelvin equivale  a {temperatura_celsius} celsius")