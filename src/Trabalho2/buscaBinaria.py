from io import SEEK_SET
import os
caminho = "cep_ordenado.dat"

size_file = os.stat(caminho).st_size

file = open("cep_ordenado.dat", 'r')

tamanho_linha = 300
numero_de_linhas = size_file//tamanho_linha #699307 linhas será o primeiro fim
procurado = int(input("Insira o cep procurado: "))
def busca(inicio, fim, procurado): 
    meio= (inicio+fim) //2
    file.seek(meio*tamanho_linha, SEEK_SET)
    
    linha = file.readline()
    cep = int( linha[290:298]) #tirando o cep
    print(cep)
    if(cep == procurado):
        print("Encontrado")
        print(linha)
    elif(inicio>fim):
        print("Nao encontrado")
    elif(procurado < cep):
        fim = meio-1
        busca(inicio, fim, procurado)
    elif(procurado>cep):
        inicio = meio+1
        busca(inicio, fim, procurado)

busca(1, numero_de_linhas, procurado)
