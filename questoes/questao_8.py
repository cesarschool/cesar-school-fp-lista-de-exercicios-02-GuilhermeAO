## QUESTÃO 8 ##
# Escreva um programa que leia uma data do usuário e calcule seu sucessor imediato.
# Por exemplo, se o usuário inserir valores que representem 2013-11-18, seu programa 
# deve exibir uma mensagem indicando que o dia imediatamente após 2013-11-18 é 
# 2013-11-19. Se o usuário inserir valores que representem 2013-11-30, o programa deve 
# indicar que o dia seguinte é 2013-12-01. Se o usuário inserir valores que representem 
# 2013-12-31 então o programa deve indicar que o dia seguinte é 2014-01-01. A data 
# será inserida em formato numérico com três instruções de entrada separadas; 
# uma para o ano, uma para o mês e uma para o dia. Certifique-se de que o seu programa 
# funciona corretamente para anos bissextos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    print("questao 8")

ano = int(input("Bote o ano ex:2018"))
mes = int(input("O mes ex:03"))
dia = int(input("Dia ex:09"))
mes1 = mes + 1
dia1 = dia + 1
if mes == 01 and dia == 31:
    print("Amanha é {} - {} - 01".format(ano, mes1, dia01))
if mes == 02 and dia ==28:
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
            print("Amanha é {} - {} - 01".format(ano, mes))
        else:
            print("Amanha é {} - {} - 01".format(ano, mes1))
if mes == 03 and dia == 31:
    print("Amanha é {} - {} - 01".format(ano, mes1,))
if mes == 04 and dia == 30:
    print("Amanha é {} - {} - 01".format(ano, mes1,))
if mes == 05 and dia == 31:
    print("Amanha é {} - {} - 01".format(ano, mes1,))
if mes == 06 and dia == 30:
    print("Amanha é {} - {} - 01".format(ano, mes1,))
if mes == 07 and dia == 31:
    print("Amanha é {} - {} - 01".format(ano, mes1,))
if mes == 08 and dia == 31:
    print("Amanha é {} - {} - 01".format(ano, mes1,))
if mes == 09 and dia == 30:
    print("Amanha é {} - {} - 01".format(ano, mes1,))
if mes == 10 and dia == 31:
    print("Amanha é {} - {} - 01".format(ano, mes1,))
if mes == 11 and dia == 30:
    print("Amanha é {} - {} - 01".format(ano, mes1,))
if mes == 12 and dia == 31:
    print("Amanha é {} - 01 - 01".format(ano +1))

    
if __name__ == '__main__':
    main()
