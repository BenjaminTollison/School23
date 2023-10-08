from manim import *
import scipy
import numpy as np
import matplotlib.pyplot as plt

def Orbit_ODE(time:float(),x_vector,gravitational_parameter:float(),dummy_variable):
  dot_r = x_vector[3:6]
  dot_v = (-gravitational_parameter/(np.linalg.norm(x_vector[0:3]))**3) * x_vector[0:3]
  dot_x = np.hstack((dot_r,dot_v))
  return dot_x

# Problem 1a
r = np.array([-6755.6,6411.11,-5585.66])
v = np.array([-3.74170,5.63902,-0.972395])
earth_gravitational_parameter = 3.986004354360959*10**5
r_magnitude = np.linalg.norm(r)
v_magnitude = np.linalg.norm(v)
h = np.cross(r,v)
h_hat = h / np.linalg.norm(h)
e = np.cross(v,h)/earth_gravitational_parameter - r/r_magnitude
e_magnitude = np.linalg.norm(e)
e_hat = e/e_magnitude
specific_mechanical_energy = v_magnitude**2/2 - earth_gravitational_parameter/r_magnitude
e_magnitude = np.linalg.norm(e)
a = -earth_gravitational_parameter/(2*specific_mechanical_energy)
p = a*(1-e_magnitude**2)
p_hat = np.cross(h,e) / np.linalg.norm(np.cross(h,e))
orbit_period = ((2*np.pi)/np.sqrt(earth_gravitational_parameter))*a**(3/2)
true_anomoly = np.linspace(0,2*np.pi,1000)
r_conic = lambda nu: p / (1+e_magnitude*np.cos(nu))
x_exact = lambda nu: (np.cos(nu)) * r_conic(nu)
y_exact = lambda nu: (np.sin(nu) * r_conic(nu))

combined_vector = np.zeros(6)
for i in range(3):
  combined_vector[i], combined_vector[i+3] = r[i], v[i]
numerical_solution = scipy.integrate.solve_ivp(Orbit_ODE,(0,orbit_period),combined_vector,method='RK45',args=(earth_gravitational_parameter,2),rtol=1e-12,atol=1e-12)
x,y,z = numerical_solution.y[0],numerical_solution.y[1],numerical_solution.y[2]
r_numerical = np.zeros((len(x),3))
x_perifocal = np.zeros(len(x))
y_perifocal = np.zeros(len(x))
z_perifocal = np.zeros(len(x))
perifocal_dict = {'x':[],'y':[],'z':[]}
for i in range(len(x)):
  r_numerical[i] = np.array([x[i],y[i],z[i]])
  perifocal_dict['x'].append(np.dot(r_numerical[i],e_hat))
  perifocal_dict['y'].append(np.dot(r_numerical[i],p_hat))
  perifocal_dict['z'].append(np.dot(r_numerical[i],h_hat))
import pandas as pd
pd.DataFrame(perifocal_dict).to_csv('Perifocal-cooridnates.csv')

class FirstOrbitGraph(Scene):
  def construct(self):
    index = ValueTracker(1)
    axis = Axes(x_range=[-30000,5000,5000],y_range=[-15000,15000,5000]).add_coordinates()
    axis_label = axis.get_axis_labels(x_label=MathTex('\\hat{e}'),y_label=MathTex('\\hat{p}'))
    orbit_dot = always_redraw(lambda:Dot(color=BLUE_B).move_to(axis.c2p(perifocal_dict['x'][int(index.get_value()-1)],perifocal_dict['y'][int(index.get_value()-1)])))
    title = Tex('Problem 1a').next_to(axis,UP,buff=-.2)
    traced_orbit = TracedPath(lambda:axis.c2p(perifocal_dict['x'][int(index.get_value()-1)],perifocal_dict['y'][int(index.get_value()-1)]))
    self.play(Create(axis),run_time = 2)
    self.play(Write(title))
    self.play(Create(axis_label))
    self.add(orbit_dot,traced_orbit)
    self.play(index.animate(rate_functions=linear).set_value(len(perifocal_dict['x'])),run_time=10)
    self.wait()
    
import os
if __name__ == "__main__":
  os.system(r"manim first-orbit-animation.py FirstOrbitGraph -pqh")