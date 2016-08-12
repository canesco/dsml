'''
XKCD STYLE
'''
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np


plt.xkcd()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xticks([])
plt.yticks([])
ax.set_ylim([-30, 10])

data = np.ones(100)
data[70:] -= np.arange(30)

plt.annotate(
    'DER TAG AN DEM ICH GEMERKT\nHABE, DASS ICH BACON ESSEN\nKANN WANNIMMER ICH WILL',
    xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(5, -10))

plt.plot(data)

plt.xlabel('Zeit')
plt.ylabel('Meine Gesundheit')
plt.show()
