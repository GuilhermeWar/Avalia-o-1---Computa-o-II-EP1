# Jogo da Forca

# Import
from random import choice

# tabuleiro
tabuleiro = ['''
>>>>>>>>>>Hangman<<<<<<<<<<
____
    |
    |
    -




=========''', '''
 ____
     |
     |
     -
     O



=========''', '''
 ____
     |
     |
     -
     O
     |


=========''', '''
 ____
     |
     |
     -
     O
    /|


=========''', '''
 ____
     |
     |
     -
     O
    /|\\


=========''', '''
 ____
     |
     |
     -
     O
    /|\\
    / 

=========''', '''
 ____
     |
     |
     -
     O
    /|\\
    / \\

=========''']

# Classe
class jogo_da_forca:
    
    # Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.erros = 0
        self.lc = ""
        self.le = ""
        self.hidden = ""
        self.temp_hidden = []
    # Método para adivinhar a letra
    def letra(self, letter):
    
    # Método para verificar se o jogo terminou
    def jogo_da_forca_fim(self):
    
    # Método para verificar se o jogador venceu
    def jogoda_forca_vitoria(self):
    # Método para não mostrar a letra no board
    def palavra_chave(self):
    
    # Método para checar o status do game e imprimir o board na tela
    def print_jogo_status(self):

# Função para ler uma palavra de forma aleatória do banco de temas e suas palavras
def palavra_aleatoria():
    with open('animais.txt') as arquivo:
        linhas = arquivo.read()
        lista_de_animais = linhas.split('\n')
    with open('objetos.txt') as arquivo:
        linhas = arquivo.read()
        lista_de_objetos = linhas.split('\n')
    with open('paises.txt') as arquivo:
        linhas = arquivo.read()
        lista_de_paises = linhas.split('\n')
    lista = choice(lista_de_animais, lista_de_objetos, lista_de_paises)
    palavra = choice(lista).upper()
    return palavra
    
# Função Main - Execução do Programa
def main():
    # Objeto
    jogo = jogo_da_forca(palavra_aleatoria())
    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    # Verifica o status do jogo
    jogo.print_game_status()
    # De acordo com o status, imprime mensagem na tela para o usuário
    if jogo.jogo_da_forca_vitoria():
        print('\nParabéns! Você venceu!!')
    
    else:
        print ('\nGame over! Você perdeu.')
        print ('A palavra era ' + jogo.palavra)
    
        print ('\nFoi bom jogar com você!\n')
    # Executa o programa  
    if __name__ == "__main__":
        main()