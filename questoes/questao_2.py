## QUESTÃO 2 ##
# Uma forma de avaliar se uma pessoa está acima do peso é através do calculo do índice IMC. 
# Se o valor do IMC estiver acima de 25, significa que a pessoa está acima do peso. 
# A fórmula é: IMC = Peso(Kg) / (Altura(m)*Altura(m)). Com base na altura e peso fornecido no 
# console exiba uma mensagem determinando se uma pessoa está acima do peso.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    print("questao 2")

nome = input("Qual o nome da pessoa que vai ter o imc medido: ")
peso = float(input("Peso em KG? : "))
altura = float(input("Altura em metros? : "))
imc = peso / altura**2
if imc > 25:
    print("{}, esta acima do peso ideal e seu imc é:{:.2f}, o imc ideal e 25.".format(nome, imc))
else:
    print("{}, nao esta acima do peso e seu imc é: {:.2f}".format(nome, imc))


if __name__ == '__main__':
    main()
