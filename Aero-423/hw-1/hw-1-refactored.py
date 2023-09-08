import numpy as np
import matplotlib.pyplot as plt
import scipy

def Orbit_ODE(time:float(),x_vector,gravitational_parameter:float(),dummy_variable):
  dot_r = x_vector[3:6]
  dot_v = (-gravitational_parameter/(np.linalg.norm(x_vector[0:3])**3)) * x_vector[0:3]
  dot_x = np.hstack((dot_r,dot_v))
  return dot_x

def ProblemOne(r_vector,v_vector):
  r = r_vector
  v = v_vector
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
  p_hat = np.cross(h,e) / p
  orbit_period = ((2*np.pi)/np.sqrt(earth_gravitational_parameter))*a**(3/2)
  true_anomoly = np.linspace(0,2*np.pi,1000)
  r_conic = lambda nu: p / (1+e_magnitude*np.cos(nu))
  x_exact = lambda nu: np.cos(nu) * r_conic(nu)
  y_exact = lambda nu: np.cos(nu) * r_conic(nu)
  combined_vector = np.zeros(6)
  for i in range(3):
    combined_vector[i], combined_vector[i+3] = r[i], v[i]
  numerical_solution = scipy.integrate.solve_ivp(Orbit_ODE,(0,orbit_period),combined_vector,method='RK45',args=(earth_gravitational_parameter,2),rtol=1e-12,atol=1e-12)
  x,y,z = numerical_solution.y[0],numerical_solution.y[1],numerical_solution.y[2]
  r_numerical = np.zeros((len(x),3))
  for i in range(len(x)):
    r_numerical[i] = np.array([x[i],y[i],z[i]])
  x_perifocal = r_numerical.dot(e_hat)
  y_perifocal = r_numerical.dot(p_hat)
  z_perifocal = r_numerical.dot(h_hat)
  return z_perifocal
ProblemOne([-6755.6,6411.11,-5585.66],[-3.74170,5.63902,-0.972395])