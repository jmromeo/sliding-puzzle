""" importing required libraries """
from random import sample # function to create pseudo random list 

DEBUG = 1;

class SlidingPuzzleModel:
  """ 

    Handles move requests and random board generation.


    SlidingPuzzleModel is the Model part of the MVC pattern for our
    Sliding Puzzle Game. The Model is in charge of figuring out whether
    a move requested by the user is a valid move, and if it is a valid
    move, to update the Sliding Puzzle board array with our move.
   

    Attributes:
      board_state: a 2 dimensional array holding the state of the board.

  """

  def __init__(self, size):
  """ 

    Function: __init__
    ------------------
    
    Initializes our board state array and randomly generates a sliding 
    puzzle Problem.
   

    size: array with the following format: [# of rows, # of columns]. 


    returns: nothing

  """
        
  def moveNumber(position):
  """

    Function: moveNumber
    --------------------

    Checks whether the requested number can move and updates the 
    cell array appropriately.


    position: an array containing the position of the number 
              requested to move with the following format, [row, col].


    returns: nothing

  """

  def getBoardState():
  """

    Function: getBoardState
    -----------------------

    Returns the current state of the board, in the form of a 2D array


    returns: 2D array holding board state

  """

  def generateBoard(self, num_rows, num_cols):
    """

      Function: generateBoard
      -----------------------

      Creates a new board, and updates the board state with the new board.


      size: array with the following format [# of rows, # of columns].

      
      returns: nothing 

    """
    # Generating a list of unique random numbers from 1->size 

    num_blocks = num_rows * num_cols; 

    randlist = sample(range(num_blocks), num_blocks); 


    # organizing list in a 2D array that matches the layout of the board 
    # algorithm for index is row = index / (num_rows), and 
    # col = index % (num_cols).  This will map the 1 dimensional list
    # to the 2D array in order from left to right, top to bottom

    for index in range(num_blocks):
      row                        = index / (num_rows);
      col                        = index % (num_cols);
      self.board_state[row][col] = randlist[index];
    
    if DEBUG:
      print self.board_state;  




