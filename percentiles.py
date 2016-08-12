'''
PERZENTILE UND MOMENTE
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

vals = np.random.normal(0, 0.5, 10000)

plt.hist(vals, 50)
plt.show()

np.percentile(vals, 50)  # 50% der Werte < dieser Wert, entspricht Mittelwert
np.percentile(vals, 90)  # 90% der Werte sind kleiner
np.percentile(vals, 20)


'''
MOMENTE
1. Durchschnitt
2. Varianz
3. Schiefe (linksschief v < 0)
4. Woelbung/Kurtosis
'''

print(np.mean(vals))
print(np.var(vals))
print(sp.skew(vals))
print(sp.kurtosis(vals))
