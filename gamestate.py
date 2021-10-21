import numpy as np
from random import *

class GameState:
    """
    Classe que representa o estado do jogo.
    """

    # -------------------------------------------------
    def __init__(self):
        """
        Construtor. Initializa o tabuleiro 3x3 vazio.
        """
        self.board = [[''] * 3 for n in range(3)]

    # -------------------------------------------------
    def save(self):
        return ';'.join([';'.join(x) for x in self.board])

    # -------------------------------------------------
    def restore(self, data):
        self.board = np.reshape(data.split(';'), (3,3)).tolist()

    # -------------------------------------------------
    def print(self):
        print("+---+---+---+")
        for row in self.board:
            print('|{}|{}|{}|'.format(row[0].center(3, ' '), row[1].center(3, ' '), row[2].center(3, ' ')))
            print("+---+---+---+")

    # -------------------------------------------------
    def move(self, row, col, piece):
        # Valida os parâmetros de entrada
        if row < 0 or row > 2:
            raise RuntimeError('Número de linha inválido: {}'.format(row))
        if col < 0 or col > 2:
            raise RuntimeError('Número de coluna inválido: {}'.format(col))
        piece = piece.lower()
        if piece != 'x' and piece != 'o':
            raise RuntimeError('Peça inválida: {}'.format(piece))

        # Verifica se a posição jogada está vazia
        if self.board[row][col] != '':
            raise RuntimeError('Posição do tabuleiro já preenchida: {}x{}'.format(row, col))

        # Faz a jogada
        self.board[row][col] = piece

    # -------------------------------------------------
    def moveRandom(self, piece):
        # Cria uma lista com as posições vazias
        options = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '':
                    options.append((row, col))

        # Faz uma permutação aleatória nessa lista
        shuffle(options)

        # Faz a jogada na primeira posição da lista
        if len(options) > 0:
            row = options[0][0]
            col = options[0][1]
            self.move(row, col, piece)
