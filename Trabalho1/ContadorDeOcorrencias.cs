using System;
using System.IO;
using System.Text;

namespace Arquivo
{
    class Program
    {

        static public void UppercaseCounter(string[] text){
            Console.WriteLine("***** Numero de caracteres maiusculos*****");
            int counter = 0;
            foreach (string line in text){
                foreach(char character in line){
                     if(char.IsUpper(character)){
                        counter++;
                    }
                }
                   
            }
            Console.Write(counter);
            Console.WriteLine();
        }
        static public void LowercaseCounter(string[] text){

            Console.WriteLine("***** Numero de caracteres minusculos *****");
            int counter = 0;
            foreach (string line in text){
                foreach(char character in line){
                    if(char.IsLower(character)){
                        counter++;
                    }
                }
                
            }
            Console.Write(counter);
            Console.WriteLine();
        }
        
        static public void DigitCounterInRange(string[] text, int begin, int end){
            Console.WriteLine("***** Numeros no range {0} e {1}*****", begin, end);
            int counter = 0;
            foreach (string line in text){
                foreach(char character in line){
                    if(char.IsDigit(character)){
                        int digit = int.Parse(character.ToString());
                        if(digit >= begin && digit <= end )
                            counter++;
                    }
                }
            }
            Console.Write(counter);
            Console.WriteLine();
        }
        static public void SpaceCounter(string[] text){

            Console.WriteLine("***** Número de espaços *****");
            
            int counter = 0;
            foreach (string line in text){
                foreach(char character in line){
                    if(char.IsWhiteSpace(character))
                        counter++;
                }
                
            }
            Console.WriteLine(counter);
            Console.WriteLine();
        }
        static public void BreakLineCounter(string[] text){

            Console.WriteLine("***** Numero de quebras de linhas *****");
            Console.WriteLine(text.Length); //O numero de linhas sempre coincide com o tamanho da matriz
            Console.WriteLine();
        }
        static void Main(string[] args)
        {

            try{
                string [] text = File.ReadAllLines(args[0], Encoding.UTF8);
                UppercaseCounter(text);
                LowercaseCounter(text);
                DigitCounterInRange(text, 0, 9);
                SpaceCounter(text);
                BreakLineCounter(text);
            
            
            } catch(IndexOutOfRangeException){
                System.Console.WriteLine("Especifique o seu o caminho do seu arquivo no argumento na execução do codigo");
            }

        }
    }
}
