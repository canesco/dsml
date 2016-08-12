'''
Mittelwert, Median und Modalwert
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

incomes = np.random.normal(33000, 15000, 10000)
print(np.mean(incomes))
print(np.median(incomes))

plt.hist(incomes, 50)
plt.show()

incomes = np.append(incomes, [10000000000])  # Hinzufuegen eines Ausreissers
print(np.mean(incomes))
print(np.median(incomes))  # Median deutlich robuster gegenueber Ausreissern

ages = np.random.randint(18, high=90, size=500)  # 500 Zufallszahlen zw. 18-90
print(stats.mode(ages))  # Modalwert
