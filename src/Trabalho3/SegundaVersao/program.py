import particionaArquivoOrdenando
import intercalaPartesV2

caminho = "cep.dat" #caminho do arquivo a ser dividido e intercalado
qtdPartes = int(input("Insira a quantidade de divisoes que deseja fazer no arquivo: "))
particionaArquivoOrdenando.main(qtdPartes, caminho)
intercalaPartesV2.main(qtdPartes)