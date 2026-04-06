# Operacoes com arquivos e diretorios em Python:
#Algoritmo Op_ArqMod-Ex38.

import os

#Declarar variaveis globais:
maior : int = 0
menor : int = 0
entrada : int = -9
linha : str = ''
dir: str = ''
arq : str = ''
txt : str = ''

#Inicio

def main():
    #Variaveis globais:
    global linha

    linha, cont = valores(linha)
    escreveArq(linha, cont)

#FIM.
        

def valores(linha):

    for cont in range(1, 101):
        entrada = int(input(f"Insira o {cont}o termo: "))
   
        while entrada < 0:
            entrada = int(input(f"Insira o {cont}o termo: "))
        
        #Fim-enquanto;

        linha = str(entrada) + '\n'
        escreveArq(linha, cont)

        if cont == 1:
            maior = entrada
            menor = entrada

        elif entrada > maior:
            maior = entrada

        elif entrada < menor:
            menor = entrada

        #Fim-se;
    #Fim-para;

    print(f"\nMaior valor: {maior}\nMenor valor: {menor}")

    linha = '\n\nMaior valor: ' + str(maior) + '\nMenor valor: ' + str(menor)

    return linha, cont

#Fim-segue.

def escreveArq(linha, cont):
    #Variaveis grobais:
    global dir
    global arq
    global txt

    dir = '/tmp/exercicios/'
    arq = 'ex38.txt'

    #Variaveis locais:
    file: str = ''
    tipo: str = ''
    enc: str = ''
    
    if not (os.path.exists(dir)):
        #Criando o diretorio.
        os.mkdir(dir)
        os.makedirs(dir, exist_ok = True)
        os.chmod(dir, 0o744) #Autorizacao de criacao, leitura e alteracao para o primeiro usuario, leitura para os demais.

    if (os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'w'
        txt = dir + arq
        enc = 'utf-8'

        if (os.path.exists(txt)) and (cont != 1):
            tipo = 'a'
       
        with open (txt, tipo, encoding=enc) as file:
            file.write(linha)
    
    else:
        print("Diretorio invalido")
    
    #Fim-se.
#Fim-segue.

if __name__ == "__main__" :
    main()
#Fim-se.
