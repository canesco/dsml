'''
MATPLOTLIB
'''

from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.01)

axes = plt.axes()
axes.set_xlim([-5, 5])  # Achsenskalierung
axes.set_ylim([0, 1.0])
axes.set_xticks([-5, -3, -1, 0, 1, 3, 5])  # Achsenbeschriftung
axes.set_yticks([0, 0.5, 1.0])
axes.grid()  # Hilfslinien
plt.xlabel('Anzahl')
plt.ylabel('Wahrscheinlichkeit')
plt.plot(x, norm.pdf(x), 'b-')  # probability density function mit Farbe
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'c--')
plt.legend(['Äpfel', 'Birnen'], loc=1)
plt.show()
# plt.savefig('grafik.png', format='png')

'''
b: blue
g: green
r: reed
c: cyan
m: magenta
y: yellow
lines: -, :, --, -.
'''
