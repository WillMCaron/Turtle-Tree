"""
Tree Fractal Generator
This program will use recursion to generate a tree using the turtle module
Programmed by Will Caron
"""

# Imports
from turtle import *
from time import sleep

# Sets cursor to be a Turtle
shape("turtle")

# Change the running speed
# lower is better, like sleeping for less time
speed(0)
DELAY = 0

def tree(size, levels, angle):
  """This Program is recursive, and will make a tree"""
  
  """
  size - the length of the lines that are used
  levels - the amount of repetitions to be performed
  angle - the angle that is turned when making the tree
  """

  if levels == 0:
    # ends loop if it completes all levels
    # changes color
    color("green")
    # creates dot
    dot(size * 0.5)
    # changes color
    color("black")
    return

  # move forward by the length specified
  forward(size)
  sleep(DELAY)
  # turn by the angle given
  right(angle)
  sleep(DELAY)

  # recursion
  tree(size * 0.8, levels-1, angle)

  # turn to do other branch
  left(angle*2)
  sleep(DELAY)

  # recursion for other branch
  tree(size * 0.8, levels-1, angle)

  # turn again
  right(angle)
  sleep(DELAY)

  # go back
  backward(size)
  sleep(DELAY)


left(90)
backward(100)
tree(60, 7, 20)
# Maintains turtle window after program completion
mainloop()
