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

class Battleship:
  def __init__(self, board):
    self.board = board

  def create_ships(self):
    for i in range(6):
      self.guess_row, self.guess_column = random.randint(0, 5), random.randint(0, 5)
      while self.board[self.guess_row][self.guess_column] == "S":
        self.guess_row, self.guess_column = random.randint(0, 5), random.randint(0, 5)
      self.board[self.guess_row][self.guess_column] = "S"
    return self.board

  def get_user_input(self):
    """ 
        player input functions are created to make sure the player selects 
        an existing row (x) and column (y) to insure the 
        instructions to the program are valid.
        """
    try:
      guess_row = input("Enter the row of the ship: e.g. 123 ")
      while guess_row not in '123456':
          print('Cannot place ship here, please select a row')
          guess_row = input("Enter the row of the ship: e.g. 123 ")

      guess_column = input("Enter the column of the ship: e.g. ABC ").upper()
      while guess_column not in "ABCDEF":
          print("Cannot place ship here, please select a column")
          guess_column = input("Enter the column of the ship: e.g. ABC ").upper()
      return int(guess_row) - 1, GameBoard.get_letters_to_numbers()[guess_column]
    except ValueError and KeyError:
      print("Input is not valid")
      return self.get_user_input()

  def count_hit_ships(self):
    """ 
        hit ships counter to start at 0, and will increase by 1 for each 
        X (direct hit) that is found on the board.
        """
    hit_ships = 0
    for row in self.board:
      for column in row:
        if column == "S":
          hit_ships += 1
    return hit_ships