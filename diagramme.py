'''
T0RTENDIAGRAMM & BALKENDIAGRAMM & SCATTERPLOT
'''
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
from pylab import randn  # fuer den scatterplot

# tortendiagram
values = [12, 55, 4, 32, 14]
colors = ['r', 'g', 'b', 'c', 'm']
explode = [0, 0, 0.2, 0, 0]
labels =['Österreich', 'Deutschland', 'Schweiz', 'Rest Europa', 'Rest Welt']
plt.pie(values, colors, labels=labels, explode = explode)
plt.title('Herkunft der Teilnehmer')
plt.show()

# balkendiagramm
values = [12, 55, 4, 32, 14]
colors = ['r', 'g', 'b', 'c', 'm']
plt.bar(range(0, 5), values, color=colors)
plt.show()

# scatterplot
X = randn(500)
Y = randn(500)
plt.scatter(X, Y)
plt.show()

# histrogram
incomes = np.random.normal(27000, 15000, 10000)
plt.hist(incomes, 50)
plt.show()

# box & whisker
# ausreisser: 1,5 mal der groesse der box entfernt
uniformSkewed = np.random.rand(100) * 100 - 40
high_outliers = np.random.rand(10) * 50 + 100
low_outliers = np.random.rand(19) * -50 - 100
data = np.concatenate((uniformSkewed, high_outliers, low_outliers))
plt.boxplot(data)
plt.show()
