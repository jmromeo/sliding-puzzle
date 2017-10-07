""" importing required libraries """
from random import sample # function to create pseudo random list

DEBUG = False;

class SlidingPuzzleModel:
  """

    Handles move requests and random board generation.


    SlidingPuzzleModel is the Model part of the MVC pattern for our
    Sliding Puzzle Game. The Model is in charge of figuring out whether
    a move requested by the user is a valid move, and if it is a valid
    move, to update the Sliding Puzzle board array with our move.


    Attributes:
      board_state: a 2 dimensional array holding the state of the board.
      neighbors:   a 2 dimensional array of lists that hold the [row, col]
                   coordinates of each of the neighboring cells


  """


  def __init__(self, size):
    """

      Function: __init__
      ------------------

      Initializes board state array and randomly generates a sliding
      puzzle Problem. Also sets up neighbors array that keeps track of
      who each cell of the boards neighboring cells are.


      size: array with the following format: [# of rows, # of columns].


      returns: nothing

    """
    # create an empty 2D array to hold the board_state

    self.num_rows = size[0];
    self.num_cols = size[1];

    self.board_state = [];

    for row in range(self.num_rows):
      self.board_state.append([]);
      for column in range(self.num_cols):
        self.board_state[row].append(0);

    self.generateBoard(self.num_rows, self.num_cols);
    self.__generateNeighbors(self.num_rows, self.num_cols);


  def checkWin(self):
    """

      Function: checkWin
      --------------------

      Checks whether the user has won. Returns true if all numbers
      are in the correct position and false otherwise.

      returns: True if all numbers are in correct position, false
               otherwise.

    """
    checknum = 0;

    for row in range(self.num_rows):
      for col in range(self.num_cols):

        # if we've reached the last item then we know that we've won, so break!
        if ((row == (self.num_rows-1)) and (col == (self.num_cols-1))):
            break;

        checknum = (row * (self.num_cols)) + col + 1;
        if (checknum != self.board_state[row][col]):
            return False;

    return True;


  def moveNumber(self, position):
    """

      Function: moveNumber
      --------------------

      Checks whether the requested number can move and updates the
      board state appropriately.


      position: an array containing the position of the number
                requested to move with the following format, [row, col].


      returns: nothing

    """
    row = position[0];
    col = position[1];

    neighbors = self.neighbors[row][col];

    for neighbor_pos in neighbors:
      xpos         = neighbor_pos[0];
      ypos         = neighbor_pos[1];
      neighbor_num = self.board_state[xpos][ypos];

      if neighbor_num == 0:
        my_num = self.board_state[row][col];

        self.board_state[row][col]   = 0;
        self.board_state[xpos][ypos] = my_num;
        break;


  def getBoardState(self):
    """

      Function: getBoardState
      -----------------------

      Returns the current state of the board, in the form of a 2D array.


      returns: 2D array holding board state.

    """
    return self.board_state;


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
    randlist   = sample(range(num_blocks), num_blocks);


    # organizing list in a 2D array that matches the layout of the board
    # algorithm for index is row = index / (num_rows), and
    # col = index % (num_cols).  This will map the 1 dimensional list
    # to the 2D array in order from left to right, top to bottom

    for index in range(num_blocks-1):
      row                        = index / (num_rows);
      col                        = index % (num_cols);
      self.board_state[row][col] = randlist[index];

    if DEBUG == True:
      print self.board_state;


  def __generateNeighbors(self, num_rows, num_cols):
    """

      Function: generateBoard
      -----------------------

      Updates the neighbor member variable to hold a list of the
      neighboring cells for each cell on the board.


      num_rows: number of rows on the board
      num_cols: number of columns on the board


      returns: nothing

    """
    self.neighbors = [];

    for row in range(num_rows):
      self.neighbors.append([]);
      for col in range(num_cols):
        neighbors = [];

        if (row - 1) >= 0:
          neighbors.append([row - 1, col]);

        if (row + 1) < num_rows:
          neighbors.append([row + 1, col]);

        if (col - 1) >= 0:
          neighbors.append([row, col - 1]);

        if (col + 1) < num_cols:
          neighbors.append([row, col + 1]);

        self.neighbors[row].append(neighbors);

    if DEBUG == True:
      for row in range(num_rows):
        for col in range(num_cols):
          neighbors = self.neighbors[row][col]
          print self.neighbors[row][col];




