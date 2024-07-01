# 14)A importancia de R$ 780.000,00 sera dividida entre 3 ganhadores de um concurso. ˆ
  #Sendo que da quantia total:
  #O primeiro ganhador recebera 46%;
  # O segundo recebera 32%; 
  # O terceiro recebera o restante;
  #Calcule e imprima a quantia ganha por cada um dos ganhadores
    
    
    # resolucao do exercicio
    
montante = float(78000000)
primeiro = float(montante*0.46)
segundo = float(montante*0.32)
terceiro = float(montante*0.22)
valor_total = primeiro+segundo+terceiro


print(f"\n O Primeiro recebe {primeiro}")
print(f"\n O segundo recebe {segundo}")
print(f"\n O terceiro recebe {terceiro}")
print(f" \n o valor total recebido é {valor_total}")