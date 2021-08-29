using System;
using System.IO;
using System.Text;

namespace Arquivo
{
    class Program
    {

        static public void UppercaseCounter(string text){
            Console.WriteLine("***** Numero de caracteres maiusculos*****");
            int counter = 0;
            foreach (char character in text){
                if(char.IsUpper(character)){
                    counter++;
                }
            }
            Console.Write(counter);
            Console.WriteLine();
        }
        static public void LowercaseCounter(string text){

            Console.WriteLine("***** Numero de caracteres minusculos *****");
            int counter = 0;
            foreach (char character in text){
                if(char.IsLower(character)){
                    counter++;
                }
            }
            Console.Write(counter);
            Console.WriteLine();
        }
        
        static public void DigitCounterInRange(string text, int begin, int end){
            Console.WriteLine("***** Numeros no range {0} e {1}*****", begin, end);
            int counter = 0;
            foreach (char character in text){
                if(char.IsDigit(character)){
                    int digit = int.Parse(character.ToString());
                    if(digit >= begin && digit <= end )
                        counter++;
                }
            }
            Console.Write(counter);
            Console.WriteLine();
        }
        static public void SpaceCounter(string text){

            Console.WriteLine("***** Número de espaços *****");
            int counter = 0;
            foreach (char character in text){
                if(char.IsWhiteSpace(character))
                    counter++;
            }
            Console.WriteLine(counter);
            Console.WriteLine();
        }
        static public void BreakLineCounter(string text){

            Console.WriteLine("***** Numero de quebras de linhas *****");
            int counter = 0;
            foreach (char character in text){
                if(character.CompareTo('\n') == 0)
                    counter++;
            }
            Console.WriteLine(counter);
            Console.WriteLine();
        }
        static void Main(string[] args)
        {
            byte[] textByte =File.ReadAllBytes(args[0]); //Pega o numero de bytes do caminho q está no argumento
            string text= Encoding.UTF8.GetString(textByte); // Converti para string porque estava dando problema com o Ç e outros q nao sao originarias da lingua inglesa
            
            UppercaseCounter(text);
            LowercaseCounter(text);
            DigitCounterInRange(text, 0, 9);
            SpaceCounter(text);
            BreakLineCounter(text);
            //obs: O breakLine também eh contado como 2 espaços!
        }
    }
}
