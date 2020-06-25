# -*- coding: utf-8 -*-

# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:


    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.posForca = 0
        self.correct = []
        self.wrong = []

    # Método para adivinhar a letra
    def guess(self, letter):
        if letter in self.word and letter not in self.correct:
            self.correct.append(letter)
        elif letter not in self.word and letter not in self.wrong:
            self.wrong.append(letter)
            self.posForca += 1
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if self.posForca == 6:
            return True
        elif self.hide_word() == self.word:
            return True
        else:
            return False

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if self.hide_word() == self.word:
            return True
        else:
            return False

    # Método para não mostrar a letra no board
    def hide_word(self):
        hide_word = ''
        for l in self.word:
            if l in self.correct:
                hide_word += l
            else:
                hide_word += '_'
        return hide_word

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[self.posForca])


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        game.print_game_status()
        print(f'\nPalavra: {game.hide_word()}')
        print('\nLetras erradas:')
        for l in game.wrong:
            print(l)
        print('\nLetras corretas:')
        for l in game.correct:
            print(l)
        letter = input('\nDigite uma letra: ')
        game.guess(letter)
    # Verifica o status do jogo
    game.print_game_status()
    print(f'\nPalavra: {game.hide_word()}')
    print('Letras erradas:')
    for l in game.wrong:
        print(l)
    print('Letras corretas:')
    for l in game.correct:
        print(l)

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()


