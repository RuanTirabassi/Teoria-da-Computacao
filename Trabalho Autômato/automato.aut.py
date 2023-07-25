import json
import csv
import sys

argvs = sys.argv
arquivo1 = argvs[1]
arquivo2 = argvs[2]
#arquivo3 = argvs[3]

with open(arquivo1, 'r') as arquivo_json:
    arq_json = json.load(arquivo_json)

with open(arquivo2, 'r') as arquivo_csv:
    csv = csv.reader(arquivo_csv)

    print(arq_json['initial'])
    print(arq_json['final'][1])
    print(arq_json['transitions'][2]['to'])
