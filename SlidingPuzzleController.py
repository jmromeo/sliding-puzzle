import pygame;
from SlidingPuzzleModel import SlidingPuzzleModel
from SlidingPuzzleView import SlidingPuzzleView

DEBUG = False;

class SlidingPuzzleController:
  """

    Interface between the Model and View.


    SlidingPuzzleController is the Controller part of the MVC pattern
    for our Sliding Puzzle Game. The Controller is in charge of
    monitoring user input, asking the Model to update the board state
    when the user requests a move, and asking the View to display the
    change of board state to the user.


    Attributes:
      None

  """

  def __init__(self, view, model):
    """

      Function: __init__
      ------------------

      Asks Model to create a random board state, then asks View to display
      that board state to the user. Also begins listening for user input,
      such as quitting out of pygame or move requests from user.


      view:  instance of SlidingPuzzleView
      model: instance of SlidingPuzzleModel


      returns: nothing

    """
    board_state = model.getBoardState();
    view.updateBoard(board_state);

    if DEBUG == True:
      print board_state;

    self.__run(view, model);


  def __run(self, view, model):
    """

      Function: __run
      ---------------

      Begins listening for user input. If the user clicks on a square,
      the Controller asks the View for the row and column indices of the
      board given the pixel coordinates of where the user clicked. If
      the user clicked on a square on the board, the Controller
      will ask the Model to determine whether the attempted move is a
      valid move or not, and will update the state of the board
      appropriately. The Controller then asks the View to display the
      new board state to the user.


      view:  instance of SlidingPuzzleView
      model: instance of SlidingPuzzleModel


      returns: nothing

    """
    done = False;

    while done == False:

      for event in pygame.event.get():

        # kill game if x button is clicked on window
        if event.type == pygame.QUIT:
          done = True;

        # kill game if escape key is pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True;

        # if mouse button was pressed, decide whether a move is valid.
        # if there is a valid move, make the move and check if the move
        # results in a win. If it does result in a win, notify the user.
        elif event.type == pygame.MOUSEBUTTONDOWN:
          pos    = pygame.mouse.get_pos();
          col_pos = pos[0];
          row_pos = pos[1];

          index = view.getIndices(row_pos, col_pos);

          if index[0] != -1:
            model.moveNumber(index);
            board_state = model.getBoardState();

            view.updateBoard(board_state);

            if (model.checkWin()):
                view.victory();
                done = True;


    pygame.quit();




