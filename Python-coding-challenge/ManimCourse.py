from manim import *

class Test(Scene):
  def construct(self):
    circ = Circle(radius=3,color=BLUE)
    self.play(Create(circ))