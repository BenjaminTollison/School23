# Task 1
Determine the trim AoA, tail incidence angle, equilibrium thrust, and the normal force with the following system of equations in the body-axis system:
$$\sum{F_X} = 0 = T_0 - W\sin\alpha_0 + L_{WF}\sin\alpha_0-D_0\cos\alpha_0 + L_H\sin(\alpha_0-\epsilon)$$
$$\sum{F_Z}=0 = -F_{N_0} + W\cos\alpha_0 - L_{WF}\cos\alpha_0-D_0\sin\alpha_0 - L_H\cos(\alpha_0-\epsilon)$$
$$\sum{M_{cg}}= 0 = F_{N_0}(X_{cg}-X_{inlet}) - L_{WF}(X_{AC_{WF}}-X_{cg})\cos\alpha_0 - D_0(X_{AC_{WF}}-X_{cg})\sin\alpha_0 - L_{H}(X_{AC_{H}}-X_{cg})\cos(\alpha_0-\epsilon)$$
## Finding $L_{WF}$
-Neglecting the lift from the fuselage
$$L_{WF} = L_W = q_\infty S_W C_{L_W}$$
- Find $C_{L_W} \approx C_{L_{W0}} + C_{L_{\alpha,W}} \alpha_0|C_{L_{W0}}=0,{symmetry}$
### Finding $C_{L_{\alpha,W}}$
- Find Taper ratio $\lambda = \frac{2S_w}{bc_r}$
- Find SweepAngle of the LE: $\Lambda_{LE} = \tan^{-1}\left(\tan{\Lambda_{c/4}} + \frac{1}{AR}\frac{1-\lambda}{1+\lambda}\right)$
- Find SweepAngle of the c/2: $\Lambda_{c/2} = \tan^{-1}\left(\tan{\Lambda_{LE}} - \frac{2}{AR}\frac{1-\lambda}{1+\lambda}\right)$
- Find $C_{l_\alpha} = \frac{2\pi}{\sqrt{1-M_\infty^2}}$
- Find Beta/k constants: $\beta = \sqrt{1-M^2}$, $k = \frac{C_{l_\alpha}}{2\pi}$
- plug into equation:
$$C_{L_\alpha} = \frac{2\pi AR}{2+\sqrt{\frac{AR^2\beta^2}{k^2}\left(1+\frac{\tan^2{\Lambda_{c/2}}}{\beta^2}\right)+4}} $$
### Find $q_\infty$
$$q_\infty = \frac{1}{2} \rho_\infty v_\infty^2$$
- Get speed of sound from the tables: $a = 296.5338[m/s]$
- Find $v_\infty$ from $M = \frac{v_\infty}{a}$
- Get the $\rho_\infty$ with isentropic equation
  - $\frac{\rho_0}{\rho} = \left(1+\frac{\gamma-1}{2}M^2\right)^\frac{1}{\gamma-1}$
  - $\rho_0 = 7.3654\cdot10^{-4} [sl/ft^3] = 0.3795971165326[kg/m^3]$

$$\therefore L_{WF} = q_\infty S_W C_{L_{\alpha,W}} \alpha_0$$