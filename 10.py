# 10) Leia uma velocidade em km/h (quilometros por hora) e apresente-a convertida em m/s ˆ
#(metros por segundo). A formula de conversão:  M = K/3.6, sendo K a velocidade em
#km/h e M em m/s.


# Resolução 
#dados de Entrada : Valores da Velocidade em Km/h 
#dados de Saida : valor da velocidade convertido em m/s

velocidade_kmh = float(input("Digite o valor da velocidade em Km/H : "))
velocidade_ms =float(velocidade_kmh*3.6)

print(f" {velocidade_kmh} Km/h equivale a {velocidade_ms} m/s")