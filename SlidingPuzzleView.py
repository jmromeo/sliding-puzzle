import pygame;

DEBUG = 1;

BLACK = (  0,   0,   0);
WHITE = (255, 255, 255);

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
      
      Creates and displays an empty board


      num_rows: number of rows on board
      num_cols: number of columns on board


      returns: nothing

    """
    board_size = [RESOLUTION[1] * .9, RESOLUTION[1] * .9];
    margin     = 5;

    cell_width  = (board_size[0] / num_cols) - (2 * margin);
    cell_height = (board_size[1] / num_rows) - (2 * margin);
    cell_size   = [cell_width, cell_height];

    for row in range(num_rows):
      for col in range(num_cols):
        col_pos  = (margin + cell_width)  * col + margin;
        row_pos  = (margin + cell_height) * row + margin;
        cell_pos = [col_pos, row_pos];
        
        pygame.draw.rect(self.screen, WHITE, [cell_pos, cell_size]);

    pygame.display.flip();


  def updateBoard(self, board_state):
    """

      Function: updateBoard
      ---------------------

      Draws the board based on the new board state. 


      board_state: a 2D array containing the state of the board


      returns: nothing


    """

  def run():
    """ 

      Function: run
      -------------

      Starts capturing user input and triggers event handler when user
      attempts to move a piece.


      returns: nothing

    """

