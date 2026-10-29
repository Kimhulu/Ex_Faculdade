"""
EXERCÍCIO FICHEIROS: Construa um programa em Python que:
Armazena e lê frutas de um ficheiro indicado pelo utilizador.

(Utilize Listas para guardar as linhas/frutas do ficheiro)

Exemplo de ecrã:

PROGRAMA FRUTAS

Nome do ficheiro a ler/escrever: _


Ficheiro "frutas.txt" preparado!
* Opções:
1) Ler o ficheiro
2) Acrescentar ao ficheiro
3) Criar/Sobrescrever o ficheiro
0) Sair
"""

print("PROGRAMA FRUTAS", "\n")
nome = input("Nome do ficheiro a ler/escrever: ")

ficheiro = open(nome, "a")

print(f'\nFicheiro "{nome}" preparado!')

opcao = -1
while opcao != 0:
    print("\nOpções:")
    print("1) Ler o ficheiro")
    print("2) Acrescentar ao ficheiro")
    print("3) Criar/Sobrescrever o ficheiro")
    print("0) Sair")

    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        ficheiro = open(nome, "r")
        frutas = ficheiro.readlines()
        print("\nConteúdo do ficheiro:")
        for fruta in frutas:
            print(fruta.strip())
        ficheiro.close()

    elif opcao == 2:
        fruta = input("\nDigite o nome da fruta a acrescentar: ")
        ficheiro = open(nome, "a")
        ficheiro.write(fruta + "\n")
        ficheiro.close()
        print(f'Fruta "{fruta}" acrescentada ao ficheiro.', "\n ")

    elif opcao == 3:
        ficheiro = open(nome, "w")
        frutas = []

        frutas = input("\nDigite os nomes das frutas (separadas por vírgula): ").split(",")
        for fruta in frutas:
            ficheiro.write(fruta.strip() + "\n")

        print(f'Ficheiro "{nome}" criado/sobrescrito.')
        ficheiro.close()

    elif opcao == 0:
        print("\nPrograma encerrado.")

    else:
        print("\nOpção inválida. Tente novamente.")
