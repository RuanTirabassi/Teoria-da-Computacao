# Simulador de Automato Deterministico
### Descrição
* Automato Finito Determinisco
     * A cada interação ele lê a entrada e troca para o próximo estado
     * A entrada só é aceita caso ela chegue até o estado final ou um dos estados finais
     * Caso a entrada não leve até um estado final, ela é rejeitada.
       
 ### Funcionamento
 <p>Primeiramente, o programa automato.aut.py recebe o arquivo_do_autoamto.aut.json, arquivo_de_teste.in.csv e arquivo_de_saida.out, respectivamente, que foram passados através do terminal. Posteriormente, os arquivos json e csv são abertos e lidos, para
  assim o código do autômato em si funcionar fazendo seus devidos processos e escrevendo os resultados no
  arquivo de saída.
 </p>
 
### arquivo_do_autoamto.aut.json
<p>Especificação do Autômato disponibilizado em formato JSON</p>
    
    {
    "initial": 0,
    "final": [4,5],
    "transitions": 
    [
        {
            "from": 0,
            "read": "a",
            "to": 1
        },
        {
            "from": 1,
            "read": "b",
            "to": 2
        },
        {
            "from": 2,
            "read": "a",
            "to": 3
        },
        {
            "from": 3,
            "read": "b",
            "to": 4
        },
        {
            "from": 4,
            "read": "a",
            "to": 5
        },
        {
            "from": 5,
            "read": "c",
            "to": 5
        }
    ]
    }

### arquivo_de_teste.in.csv
<p>Entradas para teste disponibilizado em CSV: PalavraDeEntrada;ResultadoEsperado(1 aceita/0 rejeita)</p>
    
    abab;1
    aabb;0
    ababac;1
    avba;0

### arquivo_de_saida.out
<p>Após a execução, o resulto foi armazenado em um arquivo de saída, conforme foi proposto: PalavraDeEntrada;ResultadoEsperado;ResultadoObtido;Tempo</p>
    
    abab;1;1;0.00000
    aabb;0;0;0.00000
    ababac;1;1;0.00000
    avba;0;0;0.00000

<p>As saidas dos segundos deram zero porque o codigo executa tão rapido, que quando faz a diferença do inicial e final, mesmo com 5 casa após a vírgula, ainda da zero.</p>

### automato.aut.py
<p>Codigo do autômato</p>

    import json
    import sys
    import csv
    import time
    
    argvs = sys.argv
    arquivo1 = argvs[1]
    arquivo2 = argvs[2]
    arquivo3 = argvs[3]
    
    # Abre o arquivo Json no modo leitura
    with open(arquivo1, 'r') as dados:
        arq_json = json.load(dados)
    
    # Lista para armazenar as strings da primeira coluna
    entradas = []
    
    # Abre o arquivo csv no modo leitura
    with open(arquivo2, "r") as csvfile:
        # Criamos o leitor CSV
        arq_csv = csv.reader(csvfile, delimiter=";")
    
        # Itera sobre as linhas do arquivo
        for linha in arq_csv:
            # Adiciona a primeira string da coluna à lista
            entradas.append(linha)
    
    # Atrbuimos uma variável para cada especificação do json, assim podendo manipular de maneira mais facíl
    initial_state = arq_json["initial"]
    final_states = arq_json["final"]
    transitions = arq_json["transitions"]
    
    # Abre o arquivo de saída em modo de escrita e escreve o resultado nele, juntamente com as entradas
    with open(arquivo3, "w") as saida:
        # Agora, vamos percorrer cada entrada da lista de entradas
        for entrada in entradas:
            # Pega o tempo ao inicio do processo de cada palavra
            tempo_inicial = time.time()
    
            atual_state = initial_state
    
            cont = 0
            wrongLetter = False
            # Vamos percorrer cada bloco do transitions no json
            for transition in transitions:
    
                # Atribui uma variavel para cada especificação do transition
                from_state = transition["from"]
                read_symbol = transition["read"]
                to_state = transition["to"]
    
                # Faz as comparações das letras do arquivo csv com as espcificações do arquivo json
                if from_state == atual_state:
    
                    if read_symbol == entrada[0][cont]:
                        atual_state = to_state
    
                        if cont < len(entrada[0]) - 1:
                            cont += 1
                        elif cont == len(entrada[0]) - 1:
    
                            break
                    else:
    
                        wrongLetter = True
                        break
    
            # Faz a verificação se aceita(1) ou rejeita(0)
            valorFinal = 0
            for final in final_states:
                if atual_state == final and not wrongLetter:
                    valorFinal = 1
            # Pega o tempo ao fim de todo o processo da palavra
            tempo_final = time.time()
    
            # Escreve a entrada original e o resultado esperado no arquivo de saída
            entrada_str = entrada[0]
            resultado_esperado = entrada[1]
    
            tempo = f"{tempo_final - tempo_inicial:.5f}"
            saida.write(
                f"{entrada_str};{resultado_esperado};{valorFinal};{tempo}\n")
        

## Execução da ferramenta
<p>A execução da ferramenta acontece a partir da linha de comando conforme foi proposto, para executar sera necessário utilizar o seguinte comando:</p>

$ python automato.aut.py arquivo_do_automato.aut.json arquivo_de_testes.in.csv arquivo_de_saida.out.csv
