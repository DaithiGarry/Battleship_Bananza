import random

class GameBoard:
  def __init__(self, board):
    self.board = board

  def get_letters_to_numbers():
    """ letters to numbers is used to identify the user column input to numbers on the grid"""
    letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}
    return letters_to_numbers

  def print_board(self):
    """ defines the appearance of the userboard and labels"""
      print("  A B C D E F")
      print("+ - - - - - - +")
      row_number = 1

      for row in range(6):
        """ defines the loop that runs through the board and registers the numbers and columns and the surrounding formatting"""
        self.board.append(['-'] * 6)
        number = 0

      for row in range(6):
        print(str(number + 1), end = '|')
        for column in range(len(self.board[number])):
          print(self.board[number][column], end= ' ')
        print('| ')  
        number += 1
      print("+ - - - - - - +")
