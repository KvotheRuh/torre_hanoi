# Aluno: Carlos Eduardo Nogueira Morciani
# Curso: Ciência da Computação


# Enunciado:
# A Torre de Hanói é um "quebra-cabeça" que consiste em uma base contendo três pinos, em um
# dos quais são dispostos alguns discos uns sobre os outros, em ordem crescente de diâmetro, de
# cima para baixo. O problema consiste em passar todos os discos de um pino para outro qualquer,
# usando um dos pinos como auxiliar, de maneira que um disco maior nunca fique em cima de outro
# menor em nenhuma situação. O número de discos pode variar sendo que o mais simples contém
# apenas três. Escreva uma função recursiva para determinar o menor número de movimentos para
# resolver o “quebra-cabeça” da Torre de Hanói e determine a quantidade mínima de movimentos
# para completar o quebra –cabeça com 7 discos.


# Função para mostrar todos os movimentos feitos pelos discos
def hanoi_torre(discos, inicio, temporario, final):
    if discos == 1:
        print(f'O disco 1 foi movido da origem {inicio} para o destino {final}')
        return
        
    else:
        hanoi_torre(discos - 1, inicio, final ,temporario)
        print(f'O disco {discos} foi movido da origem {inicio} para o destino {final}')
        return hanoi_torre(discos - 1 , temporario, inicio, final)

# Função que calcula o menor número de movimentos para resolver o quebra-cabeça
def hanoi_movimentos(num_discos):
    if num_discos == 1:
        return 1

    else:
        return 2*hanoi_movimentos(num_discos - 1) + 1

# Entrada do usúario
qtd_discos = int(input("Insira a quantidade de discos: "))
nome_origem = input("Insira o nome para a origem: ")
nome_auxiliar = input("Insira o nome para a auxiliar: ")
nome_destino = input("Insira o nome para a destino: ")

# Chamada da função hanoi_torre e o print da quantidade mínima de movimentos
hanoi_torre(qtd_discos, nome_origem, nome_auxiliar, nome_destino)
print(f"\nVocê terminou a Torre de Hanói em: {hanoi_movimentos(qtd_discos)} movimentos.")
