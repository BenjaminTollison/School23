### Benjamin Tollison ###
import numpy as np
import scipy

rho = 0.002377 # slug/ft^3
V_v = 500 # ft^2
W = 20500 # lb
I_y_cg = 55814 # slug-ft^2
S_w = 300 # ft^2
c_w = 11.32 # ft

q_infty = 0.5*rho*V_v**2
Q_hat = lambda Q: Q / (2*V_v/c_w)
C_L = lambda alpha,delta_E,Q_hat: 0.14 + .42*alpha - 4.8*alpha**2 + 0.44*delta_E + (30.5 + 41.3*alpha)*Q_hat
C_M_Ref = lambda alpha,delta_E,Q_hat: -0.02 + 0.04*alpha - 0.6*delta_E - 0.08*alpha*delta_E + 0.8*delta_E**2 + 0.5*delta_E*alpha**2 - Q_hat*(5.16+3.55*alpha + 35.9*alpha**2)

d_alpha_C_L = lambda alpha,delta_E,Q_hat: .42 - 2*4.8*alpha + 41.3*Q_hat
d_delta_E_C_L = lambda alpha,delta_E,Q_hat: 0.44
d_Q_C_L = lambda alpha,delta_E,Q_hat:  30.5 + 41.3*alpha
d_alpha_C_M_Ref = lambda alpha,delta_E,Q_hat: 0.04 - 0.08*delta_E + delta_E*alpha - Q_hat*(3.55 + 2*35.9*alpha)
d_delta_E_C_M_Ref = lambda alpha,delta_E,Q_hat: -0.6 - 0.08*alpha + 1.6*delta_E* + 0.5*alpha**2
d_Q_C_M_Ref = lambda alpha,delta_E,Q_hat: -1*(5.16+3.55*alpha + 35.9*alpha**2)

# task ii
# def NewtonSolver(functions:list,funtionsprime:list,intialguess:list,functionequals:list)->list:
#   tolerence = 1e-8
#   alpha_0,delta_E0,Q_0 = intialguess[0],intialguess[1],Q_hat(intialguess[2])
#   iteration_counter = 0
#   while tolerence <= functions[0](alpha_0,delta_E0,Q_0) - functionequals[0] or -tolerence >= functions[0](alpha_0,delta_E0,Q_0) - functionequals[0]\
#     and  tolerence <= functions[1](alpha_0,delta_E0,Q_0) - functionequals[1] or -tolerence >= functions[1](alpha_0,delta_E0,Q_0) - functionequals[1]\
#       and  tolerence <= functions[2](alpha_0,delta_E0,Q_0) - functionequals[2] or -tolerence >= functions[2](alpha_0,delta_E0,Q_0) - functionequals[2]:
#         alpha_0 = alpha_0 - functions[0](alpha_0,delta_E0,Q_0)/funtionsprime[0](alpha_0,delta_E0,Q_0)
#         delta_E0 = delta_E0 - functions[1](alpha_0,delta_E0,Q_0)/funtionsprime[1](alpha_0,delta_E0,Q_0)
#         Q_0 = Q_0 - functions[2](alpha_0,delta_E0,Q_0)/funtionsprime[2](alpha_0,delta_E0,Q_0)
#         iteration_counter += 1
#         if iteration_counter == 1e5:
#           print("max number of iterations error")
#           break
#   return [alpha_0,delta_E0,Q_0]
guess = [0,0,0]
equations_equal = [W/(q_infty*S_w),0,0]
alpha_0, delta_E0,Q_0 = 0,0,0
tolerence = 1e-4
alpha_0,delta_E0,Q_0 = scipy.optimize.newton(func=[C_L,C_M_Ref,Q_hat],x0=guess,fprime=[d_alpha_C_L(alpha_0,delta_E0,0)+d_delta_E_C_L(alpha_0,delta_E0,0),d_alpha_C_M_Ref(alpha_0,delta_E0,0)+d_delta_E_C_M_Ref(alpha_0,delta_E0,0),0])
print(alpha_0,delta_E0,Q_0)