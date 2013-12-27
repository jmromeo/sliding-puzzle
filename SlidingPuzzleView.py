import pygame;

DEBUG = 1;

BLACK = (  0,   0,   0);
WHITE = (255, 255, 255);
GREEN = ( 70, 200,   0);

RESOLUTION = [1280, 960];

class SlidingPuzzleView:
  """

    Updates GUI and handles capturing user input. 


    SlidingPuzzleView is the View part of the MVC pattern for our
    Sliding Puzzle Game. The view is in charge of creating the board
    and displaying the board_state to the user. It is also in charge
    of keeping track of user input.

    
    Attributes:
      none

  """

  def __init__(self, size):
    """ 

      Function: __init__
      ------------------
      
      Creates an empty board and initializes pygame.


      size: array with the following format: [# of rows, # of columns] 


      returns: nothing

    """
    num_rows = size[0];
    num_cols = size[1];

    pygame.init();

    self.screen = pygame.display.set_mode(RESOLUTION);
    self.screen.fill(BLACK);

    self.__createBoard(num_rows, num_cols);


  def __createBoard(self, num_rows, num_cols):
    """ 

      Function: __createBoard
      ------------------
      
      Creates and displays an empty board. 


      num_rows: number of rows on board
      num_cols: number of columns on board


      returns: nothing

    """
    # setting the board size to be proportional to the screen size,
    # and then setting the width and height of each of the cells on
    # our game board based on the board size

    self.board = [];

    board_size = [RESOLUTION[1] * .7, RESOLUTION[1] * .7];
    margin     = 5;

    cell_width  = (board_size[0] / num_cols) - (2 * margin);
    cell_height = (board_size[1] / num_rows) - (2 * margin);


    # creating 2D array (board). board contains rectangle objects
    # that cover each cell of our game board. for instance, board[0][1] 
    # contains a rectangle object with the position of our game cell at
    # row 0, col 1, and the width and height of a cell

    for row in range(num_rows):
      self.board.append([]);
      for col in range(num_cols):
        col_pos  = (margin + cell_width)  * col + margin;
        row_pos  = (margin + cell_height) * row + margin;
        rect     = pygame.Rect(col_pos, row_pos, cell_width, cell_height); 

        self.screen.fill(WHITE, rect);
        
        self.board[row].append(rect);
        
    pygame.display.flip();


  def updateBoard(self, board_state):
    """

      Function: updateBoard
      ---------------------

      Draws the board based on the new board state. 


      board_state: a 2D array containing the state of the board


      returns: nothing


    """

