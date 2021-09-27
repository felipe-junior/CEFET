from io import SEEK_SET
import struct
import os
import intercala
import time
from datetime import timedelta

import struct

def start_time_measure(message=None):
    if message:
        print(message)
    return time.monotonic()

def end_time_measure(start_time, print_prefix=None):
    end_time = time.monotonic()
    if print_prefix:
        delta = str(timedelta(seconds=end_time - start_time))
        print(print_prefix + delta)
    return delta
####Ignonar codigo acima-> está ai para medir o tempo de execução

caminho = "cep.dat"
size_file = os.stat(caminho).st_size

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
tamanhoDaLinha = registroCEP.size
numeroDelinhas = size_file // registroCEP.size 
numeroDivisoes = int(input("Numero de divisoes que deseja: "))
qtdLinhaPorDivisao = numeroDelinhas // numeroDivisoes 
versao = 0
with open(caminho,"rb") as f: #lendo arquivo
    for divisaoAtual in range(1, numeroDivisoes+1):
        listaTemp= []
        f.seek((divisaoAtual-1) * qtdLinhaPorDivisao * tamanhoDaLinha, SEEK_SET) #faz o deslocamento do ponteiro do arquivo para a divisao pertinente
        line = f.readline(tamanhoDaLinha)
        
        i = 1
        while(i <= qtdLinhaPorDivisao) and len(line)>0:
            endereco = registroCEP.unpack(line) #Gera tuplas com base na struct definida
            listaTemp.append(endereco) # adicicona o endereco a lista
            line = f.read(tamanhoDaLinha)
            i += 1
        
        listaTemp.sort(key=lambda e: e[5]) #ordena o arquivo gerado
        with open("parte_ordenada{}_{}.dat".format(versao, divisaoAtual),"wb") as file:
            for endereco in listaTemp: 
                file.write(registroCEP.pack(*endereco))


tempoInicial = start_time_measure("Começou a intercalar")
intercala.juntaArquivo(numeroDivisoes, versao)
tempoGasto = end_time_measure(tempoInicial, "Terminou em:")