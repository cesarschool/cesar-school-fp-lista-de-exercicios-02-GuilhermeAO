## QUESTÃO 5 ##
# Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é 
# Equilátero, Isósceles ou Escaleno.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    print("questao 5")

a = float(input("Valor do primeiro lado do triângulo : "))
b = float(input("Valor do segundo lado do triângulo : "))
c = float(input("Valor do terceiro lado do triângulo : "))
if a == b == c:
    print("O triângulo é Equilátero.")
elif a == b != c or a != b == c or a == c != b:
    print("O triângulo é Isósceles.")
elif a != b != c:
    print("O triângulo é Escaleno.")
    
if __name__ == '__main__':
    main()
