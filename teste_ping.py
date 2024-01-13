import os
import time

os.system
def pegar_ip():

    valor =input("Introduz o iP desejado : ")
    return valor

#funçaõ principal


def main():
    ip = pegar_ip()
    print(f" o ip introduzido foi {ip}")

    os.system("cls")
    # os.system("clear")  se for linux 
    os.system(f"ping {ip}")

main()




