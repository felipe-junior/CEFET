import math
import struct

registroCEP = struct.Struct("72s72s72s72s2s8s2s")  # CEP É P 8s
qtdDeArquivos = 8
print(math.ceil(math.log2(16)))


def intercala(arquivo1, arquivo2, versionIntercala):

    with open(arquivo1, "rb") as f1, open(arquivo2, "rb") as f2:

        file_gerado = open("intercala{}.dat".format(versionIntercala), "wb")
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

i = 1
# while (qtdDeArquivos!=1): 
j = 1
flag = 0
qtdDeArquivos = 2
while(i< qtdDeArquivos):

    if(flag ==0):
        intercala("intercala{}.dat".format(i), "intercala{}.dat".format(i+1),j)
    else: 
        intercala("cep_ordenado{}.dat".format(i), "cep_ordenado{}.dat".format(i+1),j)
    i+=2
    j += 1


qtdDeArquivos= qtdDeArquivos//2
i=0

[7,4,5,0,1,2,3]