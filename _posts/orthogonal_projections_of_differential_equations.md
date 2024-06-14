I have a speculation about where empirical distributions come from which has been a topic of personal rumination for me since the first year of my MSc thesis (*circa* 2020). It isn't scientific as far as I know, but it is the kind of thing that entertains me over a glass of beer.

The basic idea is to come up with a mathematical relationship between a hypothetical deterministic data generating process and empirical distributions. I'll focus on examples using differential equations.

## Exponential Decay

$$\frac{dx}{dt} = -kx$$

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def decay(t, y, k):
    return -k * y

k = 0.5
y0 = [10]
t_span = (0, 10)
t_eval = np.linspace(t_span[0], t_span[1], 100)

sol = solve_ivp(decay, t_span, y0, t_eval=t_eval, args=(k,))

# Plot histogram
plt.hist(sol.y[0], bins=10, edgecolor='black')
plt.xlabel('x')
plt.ylabel('Frequency')
plt.title('Histogram of x over time')
plt.show()
```

## Lotka-Volterra

This is a classic example of a predator-prey system.

$$\frac{dx}{dt} = ax - bxy$$
$$\frac{dy}{dt} = -cy + dxy$$

```python
def lotka_volterra(t, z, a, b, c, d):
    x, y = z
    dxdt = a * x - b * x * y
    dydt = -c * y + d * x * y
    return [dxdt, dydt]

a, b, c, d = 1.0, 0.1, 1.5, 0.075
y0 = [10, 5]
t_span = (0, 20)
t_eval = np.linspace(t_span[0], t_span[1], 200)

sol = solve_ivp(lotka_volterra, t_span, y0, t_eval=t_eval, args=(a, b, c, d))

# Plot histograms
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].hist(sol.y[0], bins=10, edgecolor='black')
axs[0].set_xlabel('x (prey)')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Histogram of prey population')

axs[1].hist(sol.y[1], bins=10, edgecolor='black')
axs[1].set_xlabel('y (predator)')
axs[1].set_ylabel('Frequency')
axs[1].set_title('Histogram of predator population')

plt.show()
```

## Lorenz System

This is a classic system in chaos theory.

$$\frac{dx}{dt} = \sigma (y - x)$$
$$\frac{dy}{dt} = x (\rho - z) - y$$
$$\frac{dz}{dt} = xy - \beta z$$

```python
def lorenz(t, state, sigma, rho, beta):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0
y0 = [1.0, 1.0, 1.0]
t_span = (0, 40)
t_eval = np.linspace(t_span[0], t_span[1], 10000)

sol = solve_ivp(lorenz, t_span, y0, t_eval=t_eval, args=(sigma, rho, beta))

# Plot histograms
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

axs[0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0].set_xlabel('x')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Histogram of x (Lorenz system)')

axs[1].hist(sol.y[1], bins=30, edgecolor='black')
axs[1].set_xlabel('y')
axs[1].set_ylabel('Frequency')
axs[1].set_title('Histogram of y (Lorenz system)')

axs[2].hist(sol.y[2], bins=30, edgecolor='black')
axs[2].set_xlabel('z')
axs[2].set_ylabel('Frequency')
axs[2].set_title('Histogram of z (Lorenz system)')

plt.show()
```

## SIR Model

This model has three state variables known as compartments:
- S: Susceptible
- I: Infected
- R: Recovered

$$\frac{dS}{dt} = - \beta SI$$
$$\frac{dI}{dt} = \beta SI - \gamma I$$
$$\frac{dR}{dt} = \gamma I$$

```python
def sir_model(t, y, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

beta = 0.3
gamma = 0.1
y0 = [0.99, 0.01, 0.0]
t_span = (0, 160)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

sol = solve_ivp(sir_model, t_span, y0, t_eval=t_eval, args=(beta, gamma))

# Plot histograms
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

axs[0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0].set_xlabel('S')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Histogram of S (Susceptible)')

axs[1].hist(sol.y[1], bins=30, edgecolor='black')
axs[1].set_xlabel('I')
axs[1].set_ylabel('Frequency')
axs[1].set_title('Histogram of I (Infected)')

axs[2].hist(sol.y[2], bins=30, edgecolor='black')
axs[2].set_xlabel('R')
axs[2].set_ylabel('Frequency')
axs[2].set_title('Histogram of R (Recovered)')

plt.show()
```

## Van der Pol Oscillator

The Van der Pol oscillator is a non-conservative oscillator with non-linear damping.

$$\frac{d^2x}{dt^2} = \mu (1 - x^2) \frac{dx}{dt} + x = 0$$


This can be written as a system of first-order differential equations:

$$\frac{dx}{dt} = y$$
$$\frac{dy}{dt} = \mu (1 - x^2) y - x$$

```python
def van_der_pol(t, state, mu):
    x, y = state
    dxdt = y
    dydt = mu * (1 - x**2) * y - x
    return [dxdt, dydt]

mu = 1.0
y0 = [2.0, 0.0]
t_span = (0, 20)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

sol = solve_ivp(van_der_pol, t_span, y0, t_eval=t_eval, args=(mu,))

# Plot histograms
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0].set_xlabel('x')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Histogram of x (Van der Pol Oscillator)')

axs[1].hist(sol.y[1], bins=30, edgecolor='black')
axs[1].set_xlabel('y')
axs[1].set_ylabel('Frequency')
axs[1].set_title('Histogram of y (Van der Pol Oscillator)')

plt.show()
```

## Brusselator (Chemical Oscillator)

The Brusselator model is a model for a type of autocatalytic reaction.

$$\frac{dx}{dt} = A + x^2y - (B+1) x$$
$$\frac{dy}{dt} = Bx - x^2 y$$

```python
def brusselator(t, state, A, B):
    x, y = state
    dxdt = A + x**2 * y - (B + 1) * x
    dydt = B * x - x**2 * y
    return [dxdt, dydt]

A = 1.0
B = 3.0
y0 = [1.0, 1.0]
t_span = (0, 20)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

sol = solve_ivp(brusselator, t_span, y0, t_eval=t_eval, args=(A, B))

# Plot histograms
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0].set_xlabel('x')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Histogram of x (Brusselator)')

axs[1].hist(sol.y[1], bins=30, edgecolor='black')
axs[1].set_xlabel('y')
axs[1].set_ylabel('Frequency')
axs[1].set_title('Histogram of y (Brusselator)')

plt.show()
```

## FitzHugh-Nagumo Model (Neuroscience)

The FitzHugh-Nagumo model is a simplification of the Hodgkin-Huxley model of neuron activation.

$$\frac{dv}{dt} = v - \frac{v^3}{3} - w + I$$
$$\frac{dw}{dt} = \frac{1}{\tau} (v + a - bw)$$

```python
def fitzhugh_nagumo(t, state, a, b, tau, I):
    v, w = state
    dvdt = v - (v**3) / 3 - w + I
    dwdt = (v + a - b * w) / tau
    return [dvdt, dwdt]

a = 0.7
b = 0.8
tau = 12.5
I = 0.5
y0 = [0.0, 0.0]
t_span = (0, 200)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

sol = solve_ivp(fitzhugh_nagumo, t_span, y0, t_eval=t_eval, args=(a, b, tau, I))

# Plot histograms
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0].set_xlabel('v')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Histogram of v (FitzHugh-Nagumo)')

axs[1].hist(sol.y[1], bins=30, edgecolor='black')
axs[1].set_xlabel('w')
axs[1].set_ylabel('Frequency')
axs[1].set_title('Histogram of w (FitzHugh-Nagumo)')

plt.show()
```

## Simple Harmonic Oscillator

A simple harmonic oscillator describes the motion of a mass-spring system without damping.

```python
def harmonic_oscillator(t, state, omega):
    x, v = state
    dxdt = v
    dvdt = -omega**2 * x
    return [dxdt, dvdt]

omega = 1.0
y0 = [1.0, 0.0]
t_span = (0, 20)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

sol = solve_ivp(harmonic_oscillator, t_span, y0, t_eval=t_eval, args=(omega,))

# Plot histograms
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0].set_xlabel('x')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Histogram of x (Harmonic Oscillator)')

axs[1].hist(sol.y[1], bins=30, edgecolor='black')
axs[1].set_xlabel('v')
axs[1].set_ylabel('Frequency')
axs[1].set_title('Histogram of v (Harmonic Oscillator)')

plt.show()
```

## Hodgkin-Huxley Model (Neuroscience)

The Hodgkin-Huxley model describes how action potentials in neurons are initiated and propagated. This is a simplified version for demonstration purposes.

$$C_m \frac{dV}{dt} = I - g_{Na} m^3 h (V - V_{Na}) - g_Kn^4(V-V_K)-g_L(V-V_L)$$
$$\frac{dm}{dt} = \alpha_m (1-m) - \beta_mm$$
$$\frac{dh}{dt} = \alpha_h (1 - h) - \beta_hh$$
$$\frac{dn}{dt} = \alpha_n (1 - n) - \beta_n n$$

```python
def hodgkin_huxley(t, state):
    V, m, h, n = state

    C_m = 1.0
    g_Na = 120.0
    g_K = 36.0
    g_L = 0.3
    V_Na = 115.0
    V_K = -12.0
    V_L = 10.6
    I = 10.0

    alpha_m = 0.1 * (25 - V) / (np.exp((25 - V) / 10) - 1)
    beta_m = 4.0 * np.exp(-V / 18)
    alpha_h = 0.07 * np.exp(-V / 20)
    beta_h = 1.0 / (np.exp((30 - V) / 10) + 1)
    alpha_n = 0.01 * (10 - V) / (np.exp((10 - V) / 10) - 1)
    beta_n = 0.125 * np.exp(-V / 80)

    dVdt = (I - g_Na * m**3 * h * (V - V_Na) - g_K * n**4 * (V - V_K) - g_L * (V - V_L)) / C_m
    dmdt = alpha_m * (1 - m) - beta_m * m
    dhdt = alpha_h * (1 - h) - beta_h * h
    dndt = alpha_n * (1 - n) - beta_n * n

    return [dVdt, dmdt, dhdt, dndt]

y0 = [-65.0, 0.05, 0.6, 0.32]
t_span = (0, 50)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

sol = solve_ivp(hodgkin_huxley, t_span, y0, t_eval=t_eval)

# Plot histograms
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

axs[0, 0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0, 0].set_xlabel('V')
axs[0, 0].set_ylabel('Frequency')
axs[0, 0].set_title('Histogram of V (Hodgkin-Huxley)')

axs[0, 1].hist(sol.y[1], bins=30, edgecolor='black')
axs[0, 1].set_xlabel('m')
axs[0, 1].set_ylabel('Frequency')
axs[0, 1].set_title('Histogram of m (Hodgkin-Huxley)')

axs[1, 0].hist(sol.y[2], bins=30, edgecolor='black')
axs[1, 0].set_xlabel('h')
axs[1, 0].set_ylabel('Frequency')
axs[1, 0].set_title('Histogram of h (Hodgkin-Huxley)')

axs[1, 1].hist(sol.y[3], bins=30, edgecolor='black')
axs[1, 1].set_xlabel('n')
axs[1, 1].set_ylabel('Frequency')
axs[1, 1].set_title('Histogram of n (Hodgkin-Huxley)')

plt.show()
```

## Double Pendulum

A double pendulum exhibits complex dynamic behavior and is described by a system of second-order differential equations. Here I converted it to a system of first-order differential equations.

$$\frac{\theta_1}{dt} = \omega_1$$
$$\frac{\theta_2}{dt} = \omega_2$$
$$\frac{\omega_1}{dt} = \frac{-g(2m_1+m_2)\sin (\theta_1) - m_2 g \sin (\theta_1 - 2 \theta_2) - 2 \sin (\theta_1 - \theta_2) m_2 (\omega_2^2 L_2 + \omega_1^2 L_1 \cos (\theta_1 - \theta_2)}{L1 (2m_1 + m_2 - m_2 \cos(2 \theta_1 - 2 \theta_2))}$$
$$\frac{d\omega_2}{dt} = \frac{2 \sin (\theta_1 - \theta_2) (\omega_1^2 L_1 (m_1 + m_2) + g(m_1 + m_2) \cos (\theta_1) + \omega_2^2 L_2 m_2 \cos (\theta_1 - \theta_2))}{L_2 (2 m_1 + m_2 - m_2 \cos (2 \theta_1 - 2 \theta_2))}$$

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def double_pendulum(t, state, m1, m2, L1, L2, g):
    theta1, omega1, theta2, omega2 = state
    delta = theta2 - theta1

    denominator1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta) ** 2
    denominator2 = (L2 / L1) * denominator1

    dtheta1_dt = omega1
    dtheta2_dt = omega2

    domega1_dt = ((m2 * L1 * omega1 ** 2 * np.sin(delta) * np.cos(delta) +
                   m2 * g * np.sin(theta2) * np.cos(delta) +
                   m2 * L2 * omega2 ** 2 * np.sin(delta) -
                   (m1 + m2) * g * np.sin(theta1)) / denominator1)

    domega2_dt = ((- m2 * L2 * omega2 ** 2 * np.sin(delta) * np.cos(delta) +
                   (m1 + m2) * (g * np.sin(theta1) * np.cos(delta) -
                   L1 * omega1 ** 2 * np.sin(delta) - g * np.sin(theta2))) / denominator2)

    return [dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt]

m1 = 1.0
m2 = 1.0
L1 = 1.0
L2 = 1.0
g = 9.81

y0 = [np.pi / 2, 0, np.pi, 0]  # Initial angles and angular velocities
t_span = (0, 20)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

sol = solve_ivp(double_pendulum, t_span, y0, t_eval=t_eval, args=(m1, m2, L1, L2, g))

# Plot histograms
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

axs[0, 0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0, 0].set_xlabel('theta1')
axs[0, 0].set_ylabel('Frequency')
axs[0, 0].set_title('Histogram of theta1 (Double Pendulum)')

axs[0, 1].hist(sol.y[1], bins=30, edgecolor='black')
axs[0, 1].set_xlabel('omega1')
axs[0, 1].set_ylabel('Frequency')
axs[0, 1].set_title('Histogram of omega1 (Double Pendulum)')

axs[1, 0].hist(sol.y[2], bins=30, edgecolor='black')
axs[1, 0].set_xlabel('theta2')
axs[1, 0].set_ylabel('Frequency')
axs[1, 0].set_title('Histogram of theta2 (Double Pendulum)')

axs[1, 1].hist(sol.y[3], bins=30, edgecolor='black')
axs[1, 1].set_xlabel('omega2')
axs[1, 1].set_ylabel('Frequency')
axs[1, 1].set_title('Histogram of omega2 (Double Pendulum)')

plt.show()
```

## Rössler Attractor

The Rössler attractor is another system that exhibits chaotic dynamics.

$$\frac{dx}{dt} = -y - x$$
$$\frac{dy}{dt} = x + ay$$
$$\frac{dz}{dt} = b + z (x - c)$$

```python
def rossler(t, state, a, b, c):
    x, y, z = state
    dxdt = -y - z
    dydt = x + a * y
    dzdt = b + z * (x - c)
    return [dxdt, dydt, dzdt]

a = 0.2
b = 0.2
c = 5.7
y0 = [1.0, 1.0, 1.0]
t_span = (0, 100)
t_eval = np.linspace(t_span[0], t_span[1], 10000)

sol = solve_ivp(rossler, t_span, y0, t_eval=t_eval, args=(a, b, c))

# Plot histograms
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

axs[0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0].set_xlabel('x')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Histogram of x (Rössler Attractor)')

axs[1].hist(sol.y[1], bins=30, edgecolor='black')
axs[1].set_xlabel('y')
axs[1].set_ylabel('Frequency')
axs[1].set_title('Histogram of y (Rössler Attractor)')

axs[2].hist(sol.y[2], bins=30, edgecolor='black')
axs[2].set_xlabel('z')
axs[2].set_ylabel('Frequency')
axs[2].set_title('Histogram of z (Rössler Attractor)')

plt.show()
```

## SEIR Model (Epidemiology)

The SEIR model is an extension of the SIR model, including an Exposed (E) compartment.

$$\frac{dS}{dt} = - \beta S I$$

$$\frac{dE}{dt} = \beta S I - \sigma E$$

$$\frac{dI}{dt} = \sigma E - \gamma I$$

$$\frac{dR}{dt} = \gamma I$$

```python
def seir_model(t, y, beta, sigma, gamma):
    S, E, I, R = y
    dSdt = -beta * S * I
    dEdt = beta * S * I - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return [dSdt, dEdt, dIdt, dRdt]

beta = 0.3
sigma = 0.1
gamma = 0.1
y0 = [0.99, 0.01, 0.0, 0.0]
t_span = (0, 160)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

sol = solve_ivp(seir_model, t_span, y0, t_eval=t_eval, args=(beta, sigma, gamma))

# Plot histograms
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

axs[0, 0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0, 0].set_xlabel('S')
axs[0, 0].set_ylabel('Frequency')
axs[0, 0].set_title('Histogram of S (Susceptible)')

axs[0, 1].hist(sol.y[1], bins=30, edgecolor='black')
axs[0, 1].set_xlabel('E')
axs[0, 1].set_ylabel('Frequency')
axs[0, 1].set_title('Histogram of E (Exposed)')

axs[1, 0].hist(sol.y[2], bins=30, edgecolor='black')
axs[1, 0].set_xlabel('I')
axs[1, 0].set_ylabel('Frequency')
axs[1, 0].set_title('Histogram of I (Infected)')

axs[1, 1].hist(sol.y[3], bins=30, edgecolor='black')
axs[1, 1].set_xlabel('R')
axs[1, 1].set_ylabel('Frequency')
axs[1, 1].set_title('Histogram of R (Recovered)')

plt.show()
```

## Chua's Circuit

Chua's circuit is a well-known example of a chaotic system. It is an electronic circuit that exhibits chaotic behavior and can be described by a system of three coupled nonlinear differential equations.

The equations for Chua's circuit are:

$$\frac{dx}{dt} = \alpha (y - x - h(x))$$
$$\frac{dy}{dt} = x - y + z$$
$$\frac{dz}{dt} = \beta z$$

where $h(x)$ is the piecewise linear function representing Chua's diode:

$$h(x) = m_1 x + \frac{1}{2} (m_0 - m_1) (|x+1| - |x- 1|)$$

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def chuas_circuit(t, state, alpha, beta, m0, m1):
    x, y, z = state

    # Chua's diode piecewise-linear function
    h = m1 * x + 0.5 * (m0 - m1) * (np.abs(x + 1) - np.abs(x - 1))

    dxdt = alpha * (y - x - h)
    dydt = x - y + z
    dzdt = -beta * y

    return [dxdt, dydt, dzdt]

# Parameters
alpha = 15.6
beta = 28.0
m0 = -1.143
m1 = -0.714

# Initial conditions
y0 = [0.7, 0.0, 0.0]
t_span = (0, 50)
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# Solve the differential equations
sol = solve_ivp(chuas_circuit, t_span, y0, t_eval=t_eval, args=(alpha, beta, m0, m1))

# Plot histograms
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

axs[0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0].set_xlabel('x')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Histogram of x (Chua\'s Circuit)')

axs[1].hist(sol.y[1], bins=30, edgecolor='black')
axs[1].set_xlabel('y')
axs[1].set_ylabel('Frequency')
axs[1].set_title('Histogram of y (Chua\'s Circuit)')

axs[2].hist(sol.y[2], bins=30, edgecolor='black')
axs[2].set_xlabel('z')
axs[2].set_ylabel('Frequency')
axs[2].set_title('Histogram of z (Chua\'s Circuit)')

plt.show()
```

