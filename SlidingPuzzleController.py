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
      none

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

    self.__run();


  def __run(self):
    done = False;

    while done == False:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True;

    pygame.quit();




