import numpy as np

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from matplotlib import animation

T = 20.0 
X = 10.0 

n = 300
m = 300

h = T / (n - 1)
k = X / (m - 1)

a = 0.5

U = np.zeros((n, m))

for i in range(0, n):
    U[i, 0] = np.exp(- (i * k - 0.2) ** 2)

for j in range(1, m):
    for i in range(1, n):
        U[i, j] = (k * U[i, j - 1] + a * h * U[i - 1, j]) / (k + a * h)

tn = np.zeros((m, 1))
for j in range(0, m):
    tn[j] = j * h

xn = np.zeros((n, 1))

for j in range(0, n):
    xn[j] = j * k

fig = plt.figure(1)

for i in [0, 20, 40, 60, 80, 100]:
    subfig = fig.add_subplot(1, 1, 1)
    label = 't = ' + str(tn[i][0])
    subfig.plot(xn, U[:, i], label=label)
    subfig.legend()
    subfig.grid(True)

plt.xlabel('x: position')
plt.ylabel('u: u(x, t)')
plt.title(r'$\frac{\partial u}{\partial t} + a \frac{\partial u}{\partial x} = 0$')

plt.savefig('advection-equation')

fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(-1, 1))
ax.grid()

line, = ax.plot([], [], lw=2)

time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

def init():
    global time_text

    line.set_data([], [])
    time_text.set_text('')
    return line,

def animate(i):
    global U
    global xn
    global tn

    time_text.set_text('time = %.1f' % tn[i])
    line.set_data(xn, U[:, i])

    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)
anim.save('advection-equation.mp4', fps=20, extra_args=['-vcodec', 'libx264'])
