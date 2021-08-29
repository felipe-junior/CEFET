using System;
using System.IO;
using System.Text;
class Program{

    static public int passos = 0;
    static string getCep(byte[] linha){
        string result = "";
        UTF8Encoding format = new UTF8Encoding(true);
        result = format.GetString(linha, 290, 8);
        return result;
    }
    static void buscaBinaria(int inicio, int fim, int procurado, FileStream fs, int numeroDeLinhas, int tamanhoLinha){
        int meio = (inicio+fim)/2;
        fs.Seek(tamanhoLinha*meio, SeekOrigin.Begin);
        byte []linhaAtual= new byte[tamanhoLinha];
        fs.Read(linhaAtual, 0, tamanhoLinha);
        int cepMeio = int.Parse(getCep(linhaAtual));
        passos++;
        if(inicio>fim){
            Console.WriteLine("Cep nao encontrado");
        } else if(procurado == cepMeio){
            Console.WriteLine("Encontrado");
        } else if(procurado < cepMeio){
            fim = meio-1;
            buscaBinaria(inicio, fim, procurado, fs, numeroDeLinhas, tamanhoLinha);
        }
        else if(procurado>cepMeio){
            inicio = meio+1;
            buscaBinaria(inicio, fim, procurado, fs, numeroDeLinhas, tamanhoLinha);
        }

    }
    static void Main(){
       
        FileStream fs = new FileStream("cep_ordenado.dat",FileMode.Open);
        
        int TAMANHO_LINHA = 300; //tamanho da linha em bytes do arquivo
        int NUMERO_DE_LINHAS =(int)( fs.Length /  TAMANHO_LINHA);
        System.Console.WriteLine("Insira o cep procurado: ");
        string input = Console.ReadLine();
        int procurado = int.Parse(input);
        buscaBinaria(0, NUMERO_DE_LINHAS, procurado, fs, NUMERO_DE_LINHAS, TAMANHO_LINHA);
        fs.Close();
        System.Console.WriteLine("Passos: {0}", passos);
    }
}