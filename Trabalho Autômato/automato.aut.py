import json
import sys
import csv
import time

argvs = sys.argv
arquivo1 = argvs[1]
arquivo2 = argvs[2]
arquivo3 = argvs[3]

# Abre o arquivo Json e lê os dados
with open(arquivo1, 'r') as dados:
    arq_json = json.load(dados)

# Lista para armazenar as strings da primeira coluna
entradas = []

# Abre o arquivo CSV e lê os dados
with open(arquivo2, "r") as csvfile:
    # Criamos o leitor CSV
    arq_csv = csv.reader(csvfile, delimiter=";")

    # Itera sobre as linhas do arquivo
    for linha in arq_csv:
        # Adiciona a primeira string da coluna à lista
        entradas.append(linha)

# Cria uma lista vazia que irá conter as listas de strings
lista_de_entradas = []

# Itera sobre cada palavra do vetor de strings
for palavra in entradas:
    # Separa cada letra da palavra e cria uma lista de strings
    lista_letras = list(palavra)

    # Adiciona a lista de strings à lista_de_listas
    lista_de_entradas.append(lista_letras)

# Exibe o resultado
# print(lista_de_entradas)

initial_state = arq_json["initial"]
final_states = arq_json["final"]
transitions = arq_json["transitions"]

# Agora, vamos percorrer letra por letra de cada palavra dentro das listas
for ler_lista in lista_de_entradas:
    atual_state = initial_state
    print("----------------------")

# abab;1
# ababcc;1
# abcd;1
# ababa;1

    # for letra in ler_lista:
    cont = 0
    wrongLetter = False
    for transition in transitions:
        tempo_inicial = time.time()

        from_state = transition["from"]
        read_symbol = transition["read"]
        to_state = transition["to"]

        # print(str(from_state) + "-" + str(atual_state))

        # print(str(ler_lista))
        if (from_state == atual_state):

            # print(str(read_symbol) + "-" + str(ler_lista[cont]))
            if (read_symbol == ler_lista[cont]):
                # print(str(cont) + "-" + str( len(ler_lista)-1))
                # print(str(read_symbol) + "-" + ler_lista[cont])
                atual_state = to_state
                print(atual_state)

                if (cont < len(ler_lista)-1):
                    cont += 1
                elif (cont == len(ler_lista)-1):
                    # print("opa")
                    break
            else:
                # print("off")
                wrongLetter = True
                break
        tempo_final = time.time()
        # else:
        #     print("zuo")

    print("\n")
    # print(wrongLetter)
    valorFinal = 0
    for final in final_states:
        if (atual_state == final and not wrongLetter):
            valorFinal = 1
            print(1)
    if (valorFinal == 0):
        print(0)

print(f"demorou{float(tempo_final - tempo_inicial)} seg")
