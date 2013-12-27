import pygame
from SlidingPuzzleModel import SlidingPuzzleModel
from SlidingPuzzleView import SlidingPuzzleView
from SlidingPuzzleController import SlidingPuzzleController

pygame.init();

model       = SlidingPuzzleModel([4,4]);
view        = SlidingPuzzleView([4,4]);
controller  = SlidingPuzzleController(view, model);


while True:
  """ """
