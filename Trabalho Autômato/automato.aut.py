import json
import csv

with open('arquivo_do_automato.aut.json') as arquivo_json:
    arq_json = json.load(arquivo_json)

with open('arquivo_de_testes.in.csv', 'r') as arquivo_csv:
    csv = csv.reader(arquivo_csv)

    print(arq_json['initial'])
    print(arq_json['final'][1])
    print(arq_json['transitions'][2]['to'])
