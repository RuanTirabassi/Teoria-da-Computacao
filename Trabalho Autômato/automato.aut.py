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


# Inicializa um novo vetor que irá conter as palavras separadas
entradas_separadas = []

# Itera sobre cada palavra do vetor de strings
for palavra in entradas:
    # Separa cada letra da palavra e cria um novo vetor com as letras
    entradas_palavras = list(palavra)
    
    # Adiciona o vetor de letras ao vetor_separado
    entradas_separadas.append(entradas_palavras)

# Exibe o resultado
print(entradas_separadas)

