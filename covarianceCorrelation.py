'''
KOVARIANZ UND KORRELATION
Korrelation: Kovarianz/Standardabweichung
-1 -> perfekte inverse Korrelation
1 -> perfekte Korrelation
0 -> keine Korrelation
'''

# Zusammenhang zwischen Zufallsvariablen


import matplotlib.pyplot as plt
import numpy as np


pageSpeeds = np.random.normal(3.0, 1.0, 1000)
# purchaseAmount = np.random.normal(50.0, 10.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

plt.scatter(pageSpeeds, purchaseAmount)
plt.show()
np.corrcoef(pageSpeeds, purchaseAmount)
np.cov(pageSpeeds, purchaseAmount)
