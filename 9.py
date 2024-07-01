# 9)  Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A
  #formula de conversão : K = C + 273.15, sendo C a temperatura em Celsius e K a
  #temperatura em Kelvin


# dados de entrada : o Valor da Temperatura
# dados de saida : o Valor da conversão

temperatura_celsius=float(input(" Porfavor Digite o Valor da Temperatura em Graus celsius: "))
temperatura_kelvin = float(temperatura_celsius+273.15)

print(f"{temperatura_celsius} celsius equivale  a {temperatura_kelvin} kelvin")