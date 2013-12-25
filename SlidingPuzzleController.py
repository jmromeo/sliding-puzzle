class SlidingPuzzleController:
  """

    Interface between the Model and View.


    SlidingPuzzleController is the Controller part of the MVC pattern 
    for our Sliding Puzzle Game. The Controller is in charge of 
    registering a listener with the View that will be called when
    a user attempts to make a move, and then passing the move request
    to the Model.

    
    Attributes:
      none

  """

  def __init__(self, view, model):
  """

    Function: __init__
    ------------------

    Registers listener with View, asks Model to create a Board,
    and asks the View to draw the created board. 


    view: instance of SlidingPuzzleView
    model: instnace of SlidingPuzzleModel


    returns: nothing

  """
  
  def moveRequest(position):
  """
    
    Function: moveRequest
    ---------------------

    moveRequest is to be registered as a callback function from the
    view. moveRequest takes the row position and column position of
    the requested move and sends it to the Model to update the board
    appropriately.


    position: an array containing the position of the number
              requested to move with the following format, [row, col].


    returns: nothing

  """
