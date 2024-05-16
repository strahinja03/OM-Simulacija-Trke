import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


F = 400 
m = 80
fv = 25.8 
fc = 488 
tc = 0.67  
A = 0.45  
rho = 1.293  
CD = 1.2 
w = 0  


t0 = 0  
dt = 1e-2  
t_final = 10  


t = np.arange(t0, t_final, dt)
x = np.zeros((3, len(t))) 
v = np.zeros((3, len(t))) 


for i in range(1, len(t)):
    a1 = F / m
    v[0, i] = v[0, i-1] + a1 * dt
    x[0, i] = x[0, i-1] + v[0, i] * dt

    a2 = (F - 0.5 * A * rho * CD * (v[1, i-1] - w)**2) / m
    v[1, i] = v[1, i-1] + a2 * dt
    x[1, i] = x[1, i-1] + v[1, i] * dt

    a3 = (F + fc * np.exp(-(t[i-1]/tc)**2) - fv * v[2, i-1] - 0.5 * A * rho * CD * (v[2, i-1] - w)**2) / m
    v[2, i] = v[2, i-1] + a3 * dt
    x[2, i] = x[2, i-1] + v[2, i] * dt

fig, ax = plt.subplots()

linije = []
for i in range(3):
    linija, = ax.plot([], [], marker='o')
    linije.append(linija)

ax.set_xlim(0, t_final)
ax.set_ylim(0, 100)
ax.set_xlabel('Vreme [s]')
ax.set_ylabel('Pozicija [m]')
ax.legend(['Konstantna sila, bez otpora vazduha', 'Konstantna sila, sa otporom vazduha', 'Promenljiva sila, sa otporom vazduha'])

def init():
    for linija in linije:
        linija.set_data([], [])
    return linije

def update(frame):
    for i, linija in enumerate(linije):
        linija.set_data(t[:frame], x[i, :frame])
    return linije

ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=1000/60) 

plt.show()
