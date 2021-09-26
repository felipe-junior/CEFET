import math
import struct

registroCEP = struct.Struct("72s72s72s72s2s8s2s")  # CEP É P 8s


def _intercala(arquivo1, arquivo2, versionIntercala, file_id):

    with open(arquivo1, "rb") as f1, open(arquivo2, "rb") as f2:

        file_gerado = open("parte_ordenada{}_{}.dat".format(versionIntercala, file_id), "wb")
        line1 = f1.read(registroCEP.size)
        line2 = f2.read(registroCEP.size)
        

        while((len(line1) > 0 and len(line2) > 0)):
            endereco1 = registroCEP.unpack(line1)
            endereco2 = registroCEP.unpack(line2)
            cepf1 = endereco1[5]
            cepf2 = endereco2[5]

            if(cepf1 < cepf2):
               file_gerado.write(registroCEP.pack(*endereco1))
               line1 = f1.read(registroCEP.size)
            else:
                file_gerado.write(registroCEP.pack(*endereco2))
                line2 = f2.read(registroCEP.size)
        
        while(len(line1)>0):
            endereco1 = registroCEP.unpack(line1)
            file_gerado.write(registroCEP.pack(*endereco1))
            line1 = f1.read(registroCEP.size)
        while(len(line2)>0):
            endereco2 = registroCEP.unpack(line2)
            file_gerado.write(registroCEP.pack(*endereco2))
            line2 = f2.read(registroCEP.size)
        file_gerado.close()

def juntaArquivo(qtdDeArquivos, versao):
    while(qtdDeArquivos!=1 ):
        limit = qtdDeArquivos
        print(limit)
        divisaoAtual = 1
        j = 1
        while(divisaoAtual <= limit):
            caminhoArquivo1 ="parte_ordenada{}_{}.dat".format(versao, divisaoAtual) 
            caminhoArquivo2 = "parte_ordenada{}_{}.dat".format(versao, divisaoAtual+1)
            print(caminhoArquivo1 + " -- "+ caminhoArquivo2)
            _intercala(caminhoArquivo1, caminhoArquivo2,versao+1, j)
            divisaoAtual+=2
            j+=1
        versao += 1
        qtdDeArquivos /= 2 #Divide ao meio o numero de arquivos a ser iterado