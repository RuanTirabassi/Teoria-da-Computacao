import json
import csv
import sys

argvs = sys.argv
arquivo1 = argvs[1]
arquivo2 = argvs[2]
#arquivo3 = argvs[3]

with open(arquivo1, 'r') as arquivo_json:
    arq_json = json.load(arquivo_json)
    
    print(arq_json['initial'])
    print(arq_json['final'][1])
    print(arq_json['transitions'][2]['to'])
    
# Lista para armazenar as strings da primeira coluna
entradas = []

# Abre o arquivo CSV e lê os dados
with open(arquivo2, "r") as csvfile:
    # Criamos o leitor CSV
    leitor = csv.reader(csvfile, delimiter=";")

    # Itera sobre as linhas do arquivo
    for linha in leitor:
        # Adiciona a primeira string da coluna à lista
        entradas.append(linha[0])

# Cria uma lista vazia que irá conter as listas de strings
lista_de_entradas = []

# Itera sobre cada palavra do vetor de strings
for palavra in entradas:
    # Separa cada letra da palavra e cria uma lista de strings
    lista_letras = list(palavra)
    
    # Adiciona a lista de strings à lista_de_listas
    lista_de_entradas.append(lista_letras)

# Exibe o resultado
print(lista_de_entradas)


