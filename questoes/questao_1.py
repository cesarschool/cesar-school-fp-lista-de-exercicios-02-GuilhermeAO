## QUESTÃO 1 ##
# Faça um programa que receba cinco inteiros e diga qual deles é o maior e qual o menor.
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    print("questao 1")
    n1 = int(input("Digite o primeiro numero inteiro: "))
n2 = int(input("Digite o segundo numero inteiro: "))
n3 = int(input("Digite o terceiro numero inteiro: "))
n4 = int (input("Digite o quarto numero inteiro: "))
n5 = int(input("Digite o quinto numero inteiro: "))
if n1 >= n2 and n1 >= n3 and n1 >= n4 and  n1 >= n5:
    print("{} é o maior numero.".format(n1))
elif n2 >= n1 and n2 >= n3 and n2 >= n4 and n2 >= n5:
    print("{} é o maior numero.".format(n2))
elif n3 >= n1 and n3 >= n2 and n3 >= n4 and n3 >= n5:
    print("{} é o maior numero.".format(n3))
elif n4 >= n1 and n4 >= n2 and n4 >= n3 and n4 >= n5:
    print("{} é o maior numero.".format(n4))
elif n5 >= n1 and n5 >= n2 and n5 >= n3 and n5 >= n4:
    print("{} é o maior numero.".format(n5))

if n1 <= n2 and n1 <= n3 and n1 <= n4 and n1 <= n5:
    print("{} é o menor numero.".format(n1))
elif n2 <= n1 and n2 <= n3 and n2 <= n4 and n2 <= n5:
    print("{} é o menor numero.".format(n2))
elif n3 <= n1 and n3 <= n2 and n3 <= n4 and n3 <= n5:
    print("{} é o menor numero.".format(n3))
elif n4 <= n1 and n4 <= n2 and n4 <= n3 and n4 <= n5:
    print("{} é o menor numero.".format(n4))
elif n5 <= n1 and n5 <= n2 and n5 <= n3 and n5 <= n4:
    print("{} é o menor numero.".format(n5))
    


if __name__ == '__main__':
    main()
