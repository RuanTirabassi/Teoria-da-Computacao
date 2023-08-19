## Simulador de Automato Deterministico
### Descrição
* Automato Finito Determinisco
     * A cada interação ele lê a entrada e troca para o próximo estado
     * A entrada só é aceita caso ela chegue até o estado final ou um dos estados finais
     * Caso a entrada não leve até um estado final, ela é rejeitada.
       
 ### Funcionamento
 <p>Primeiramente, o programa recebe o nome do arquivo json, css e arquivo de saída, respectivamente
  que foram passados através do terminal.Posteriormente, os arquivos json e css são abertos e lidos, para
  assim o código do autômato em si funcionar fazendo seus devidos processos e escrevendo os resultados no
  arquivo de saída.
 </p>
 
### arquivo_do_autoamto.aut.json
     {
    "initial": 0,
    "final": [
        4,
        5
    ],
    "transitions": [
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
    abab;1
    aabb;0
    ababac;1
    avba;0

### arquivo_de_saida.out
    
