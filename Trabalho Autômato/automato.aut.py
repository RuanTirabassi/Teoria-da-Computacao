import json
import csv

with open ('arquivo_do_automato.aut.json') as arq_json:
    arq =  json.load(arq_json)
    
    print(arq)

with open('arquivo_de_testes.in.csv', 'r') as arq_csv:
    ler = csv.reader(arq_csv)

    for linha in ler:
        print(linha)    