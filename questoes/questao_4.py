## QUESTÃO 4 ##
# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos 
# a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o 
# valor da prestação como sendo o valor da casa a comprar dividido pelo número de 
# meses a pagar.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    print("questao 4")

salario = float(input("Qual o seu salario? : "))
valor_casa = float(input("Qual o valor da casa? : "))
tempo_anos = int(input("Em quantos anos você pretende pagar a casa? : "))
porc_sala = salario * 0.30
tempo_meses = tempo_anos * 12
valor_de_prestação = valor_casa / tempo_meses
if valor_de_prestação > porc_sala:
    print("""EMPRESTIMO NEGADO! (A prestação esta com o valor com mais de 30% de seu salario, para ter seu emprestimo aprovado,
    o valor da parcela precisa ter 30% ou menos o valor de seu salario).""")
else:
    print("Parabens voce teve seu emprestimo aprovado.")

    
if __name__ == '__main__':
    main()
