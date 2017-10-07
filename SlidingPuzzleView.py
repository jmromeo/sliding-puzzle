import pygame;

DEBUG = False;

# colors
BLACK = (  0,   0,   0);
WHITE = (255, 255, 255);
GREEN = ( 70, 200,   0);

# game options
TEXT_COLOR       = BLACK;
BACKGROUND_COLOR = BLACK;
BOARD_COLOR      = WHITE;
FONT_SIZE        = 40;
RESOLUTION       = [1280, 960];
BOARD_RATIO      = [1.0, 1.0];
CELL_MARGIN      = 5;

class SlidingPuzzleView:
  """

    Updates GUI based on board_state.


    SlidingPuzzleView is the View part of the MVC pattern for our
    Sliding Puzzle Game. The view is in charge of creating the board
    and displaying the board_state to the user.


    Attributes:
      screen: pygame screen object that can be drawn on

      board: 2D array containing rectangles that cover each cell
             of the game board.

      board_width:  width of the entire board.
      board_height: height of the entire board.

      cell_width:  width of each cell of the game board.
      cell_height: height of each cell of the game board.

      num_rows: number of rows on the board.
      num_cols: number of columns on the board.

  """


  def __init__(self, size):
    """

      Function: __init__
      ------------------

      Creates and displays an empty board.


      Creates and displays an empty board, and updates the 2D member
      array, board, to hold rectangles that cover each of the cells of
      our game board.


      size: array with the following format: [# of rows, # of columns]


      returns: nothing

    """
    self.num_rows = size[0];
    self.num_cols = size[1];

    width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
    RESOLUTION[0] = width;
    RESOLUTION[1] = height;

    self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN);
    self.screen.fill(BACKGROUND_COLOR);

    self.__createBoard(self.num_rows, self.num_cols);


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

    board_size = [RESOLUTION[0] * BOARD_RATIO[0], RESOLUTION[1] * BOARD_RATIO[1]];

    self.cell_width  = (board_size[0] / num_cols) - (2 * CELL_MARGIN);
    self.cell_height = (board_size[1] / num_rows) - (2 * CELL_MARGIN);

    self.board_width  = board_size[0];
    self.board_height = board_size[1];

    # creating 2D array (board). board contains rectangle objects
    # that cover each cell of our game board. for instance, board[0][1]
    # contains a rectangle object with the position of our game cell at
    # row 0, col 1, and the width and height of a cell

    for row in range(num_rows):
      self.board.append([]);
      for col in range(num_cols):
        col_pos  = (CELL_MARGIN + self.cell_width)  * col + CELL_MARGIN;
        row_pos  = (CELL_MARGIN + self.cell_height) * row + CELL_MARGIN;

        rect     = pygame.Rect(col_pos, row_pos,
                               self.cell_width, self.cell_height);

        self.screen.fill(BOARD_COLOR, rect);

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
    self.screen.fill(BACKGROUND_COLOR);
    font = pygame.font.SysFont("comicsansms", FONT_SIZE);

    for row in range(self.num_rows):
      for col in range(self.num_cols):
        self.screen.fill(BOARD_COLOR, self.board[row][col]);

        if board_state[row][col] > 0:
          string          = str(board_state[row][col]);
          text            = font.render(string, True, TEXT_COLOR);

          textpos         = text.get_rect();
          textpos.centerx = self.board[row][col].centerx;
          textpos.centery = self.board[row][col].centery;

          self.screen.blit(text, textpos);


    pygame.display.flip();


  def getIndices(self, x_pos, y_pos):
    """

      Function: getIndices
      ---------------------

      Returns the row and column indices of the cell that lies at the
      cartesian coordinates [x_pos, y_pos]. Returns [-1, -1] if
      coordinates are not within the bounds of the board.


      x_pos: x coordinates of user click.
      y_pos: y coordinates of user click.


      returns: row and column indices on success, and [-1, -1] on
               failure.

    """
    row = (x_pos - CELL_MARGIN) / (CELL_MARGIN + self.cell_height);
    col = (y_pos - CELL_MARGIN) / (CELL_MARGIN + self.cell_width);

    if row > self.num_rows or col > self.num_cols:
      index = [-1, -1];

    else:
      index = [int(row), int(col)];

    return index;


  def victory(self):
    """

      Function: victory
      ---------------------

      Notifies the user they have won the game!

      returns: nothing

    """
    print "yay you won the game!"





