# Ordenação e intercalação de arquivos

## Como funciona?


O ```particionaArquivoOrdenando.py``` divide os arquivos em n divisoes advindas do input do usuário,
ordena-os e gera as partes ordenadas. Depois chama o módulo ```intercalaPartes.py``` para fazer as
intercalações das partes lendo as linhas das partes, escolhendo a linha que possui o menor cep e inserindo essa nova linha no novo arquivo ``cep_ordenado.dat``. 
Faz esssas operações até nao sobra nenhuma linha a ser comparada.

A variável ``caminho`` pode ser alterada para o arquivo dos ceps

Funciona com qualquer numero de divisoes.
Executar em program.py

