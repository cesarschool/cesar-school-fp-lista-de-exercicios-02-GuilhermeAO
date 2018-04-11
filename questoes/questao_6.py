## QUESTÃO 6 ##
# Escreva um programa que calcule a porcentagem de nucleotídeos A, C, G e T em 
# uma cadeia de DNA informada pelo usuário. Indicar também a quantidade e a 
# porcentagem de nucleotídeos inválidos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    print("questao 6")

    cadeia_dna = str(input("Digite a cadeia de DNA: "))
cont_A = cadeia_dna.count("A")
cont_C = cadeia_dna.count("C")
cont_G = cadeia_dna.count("G")
cont_T = cadeia_dna.count("T")
soma_cont = cont_A + cont_T + cont_C + cont_G
todos_carac = len(cadeia_dna)
porc_A = (100 * cont_A) / todos_carac
porc_C = (100 * cont_C) / todos_carac
porc_G = (100 * cont_G) / todos_carac
porc_T = (100 * cont_T) / todos_carac
quant_inv = todos_carac - soma_cont
porc_inv = (100 * quant_inv) / todos_carac
if quant_inv == 0:
    print("""A porcentagem de nucleotídeos A é: {}%
        de nucleotídeos C é: {}%
        de nucleotídeos G é: {}%
        de nucleotídeos T é: {}%
        Não tem nucleotídeos invalidos na cadeia de DNA informada.""".format(porc_A, porc_C, porc_G, porc_T))
else:
    print("""A porcentagem de nucleotídeos A é: {}%
        de nucleotídeos C é: {}%
        de nucleotídeos G é: {}%
        de nucleotídeos T é: {}%
        A quantidade de nucleotídeos invalidos é de {} e a porcentagem de {}%.""".format(porc_A, porc_C, porc_G, porc_T, quant_inv, porc_inv))

    
if __name__ == '__main__':
    main()
