from manim import *

class Test(Scene):
  def construct(self):
    circ = Circle(radius=3,color=BLUE)
    self.play(Create(circ))

class Pith(Scene):
  def construct(self):
    sq = Square(side_length = 5, stroke_color = GREEN, fill_color=BLUE, fill_opacity=0.75)
    self.play(Create(sq))
    self.wait()
    self.play(FadeOut(sq))

class Testing(Scene):
  def construct(self):
    name = Tex("Benjamin").to_edge(UL,buff=0.5)
    sq = Square(side_length=0.5,fill_color=GREEN,fill_opacity=0.5).shift(LEFT*3)
    tri = Triangle().scale(0.5).to_edge(DR)

    self.play(Write(name))
    self.play(DrawBorderThenFill(sq),run_time=2)
    self.play(Create(tri))
    self.wait()
    self.play(name.animate.to_edge(UR),run_time=2)
    self.play(sq.animate.scale(2),tri.animate.to_edge(DL),run_time=4)

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square(side_length=1.5,fill_color=GREEN,fill_opacity=.5)
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class Getters(Scene):
  def construct(self):
    rectangle = Rectangle(color=WHITE,height=2,width=2,fill_color=WHITE,fill_opacity=0.5).to_corner(UL)
    circle = Circle().to_edge(DOWN)
    arrow = always_redraw(lambda: Line(start=rectangle.get_center(),end=circle.get_top()).add_tip())

    self.play(DrawBorderThenFill(rectangle),Write(circle))
    self.play(Write(arrow),run_time=2)
    self.play(rectangle.animate.to_edge(UR),circle.animate.scale(.4),run_time=4)

class Updaters(Scene):
  def construct(self):
    eqn = MathTex('\\Delta{s} = c_p ln\\left(\\frac{T_2}{T_1}\\right) - R ln\\left(\\frac{P_2}{P_1}\\right)')
    box = SurroundingRectangle(
      eqn,color=RED,fill_opacity=0.1,fill_color=BLUE,buff=1
    )
    eqn_name = Tex('Change in Entropy').next_to(box,direction=UP,buff=0.25)
    first_group = VGroup(eqn,box,eqn_name).scale(0.8)
    conservation_of_mass = MathTex('\\int_\\tau \\partial_t \\rho d\\tau + \\int_\\sigma \\rho(\\vec{v} \\cdot \\hat{n})d\\sigma')
    box2 = SurroundingRectangle(
      conservation_of_mass,color=RED,fill_opacity=0.1,fill_color=BLUE,buff=1
    )
    eqn_name2 = Tex('Conservation of Mass').next_to(box2,direction=UP,buff=0.25)
    second_group = VGroup(conservation_of_mass,box2,eqn_name2).shift(DOWN*2).scale(0.8)
    self.play(Write(first_group),run_time=3)
    self.play(first_group.animate.shift(UP*2),run_time=2)
    self.wait()
    self.play(Write(second_group),run_time=4)
    
class ValueTrackers(Scene):
  def construct(self):
    k = ValueTracker(5)
    number = always_redraw(lambda: DecimalNumber().set_value(k.get_value()))

    self.play(FadeIn(number))
    self.wait()
    self.play(k.animate.set_value(0),run_time=4,rate_func=smooth)

class TestGraph(Scene):
  def construct(self):
    plane = NumberPlane(x_range=[-4,4,2],x_length=7,y_range=[-16,16,4],y_length=7).to_edge(DOWN).add_coordinates()
    parabola = plane.plot(lambda x: x**3 - 4, x_range=[-4,4],color=GREEN)
    sine = plane.plot(lambda x: np.sin(x),x_range=[-4,4],color=RED)
    labels = plane.get_axis_labels(x_label='x',y_label='f(x)')

    self.play(DrawBorderThenFill(plane))
    self.play(Create(labels))
    self.play(Create(parabola),run_time=2)
    self.play(Write(MathTex('f(x)=x^3 - 4').scale(0.4).next_to(parabola,direction=RIGHT,buff=.5).shift(LEFT*1.5).shift(UP*2)))
    self.wait()
    self.play(Write(sine),run_time = 2)
    self.play(Write(MathTex('f(x)=\\sin(x)').scale(.4).next_to(sine,direction=RIGHT,buff=.5).shift(LEFT).shift(DOWN*0.5)))
    self.play(FadeIn(Tex('Example Graph').next_to(plane,DOWN,buff=0.3).scale(1).shift(UP)),run_time=2)
    self.wait()