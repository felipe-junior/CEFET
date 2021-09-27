import time
import os
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
####Ignonar codigo acima->está ai para medir o tempo de execução



def pathFormat(versao, qtd):
    paths = []
    for i in range(1,qtd+1):
        paths.append("parte_ordenada{}_{}.dat".format(versao, i))
    return paths

def encontraMenorIndex(cepList):
    menor = cepList.__len__()-1
    for i in range(0, cepList.__len__()):
        if(cepList[i] < cepList[menor]):
            menor = i
    return menor
def getCep(endereco):
    return registroCEP.unpack(endereco)[5]

def getCepList(listEndereco): #retorna uma lista de ceps que foram retidados das linhas dos arquivos
    listCeps = []
    for endereco in listEndereco:
        listCeps.append(getCep(endereco))
    return listCeps


registroCEP = struct.Struct("72s72s72s72s2s8s2s")

def main(qtdPartes):

    #qtdPartes = int(input("Insira a quantidade de partes: "))

    listCaminho= [*pathFormat(0, qtdPartes)]
    listArquivosAbertos = []
    tempoInicial = start_time_measure("Começou a intercalar")

    for i in range(qtdPartes): #Abre todos os arquivos
        listArquivosAbertos.append(open(listCaminho[i], 'rb'))



    arquivoOrdenado = open('cep_ordenado.dat', 'wb')
    enderecoList = [] #Responsavel por armazenar as linha das divisoes 


    for i in range(0, qtdPartes):#Esse for adiciona as linhas de cada arquivo no enderecoList. (primeira leitura)
            enderecoList.append(listArquivosAbertos[i].read(registroCEP.size))

    while(listArquivosAbertos.__len__() != 0):
        
        cepList = getCepList(enderecoList)
        menor = encontraMenorIndex(cepList)
        
        arquivoOrdenado.write(enderecoList[menor])
        enderecoList[menor] = listArquivosAbertos[menor].read(registroCEP.size)
        if(len(enderecoList[menor]) ==0): #Se nao ha mais linhas na parte ela eh retirada do enderecoList e arquivosAbertos
            enderecoList.pop(menor)
            listArquivosAbertos[menor].close()
            listArquivosAbertos.pop(menor)
        
    tempoGasto = end_time_measure(tempoInicial, "Terminou em:")

    resultados = open("resultados.dat", 'a')

    resultados.write("Partes: {}    | TempoGasto: {}\n".format(qtdPartes, tempoGasto))
    resultados.close()
