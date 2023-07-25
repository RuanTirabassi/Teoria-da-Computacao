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
    
with open(arquivo2, 'r') as arquivo_csv:
    arq_csv = csv.reader(arquivo_csv)
    for line_number, content in enumerate(arq_csv): 
        colunas = content.split(';')
        p = list(f"{colunas[0]}")

        for n in p:
            print(n)
