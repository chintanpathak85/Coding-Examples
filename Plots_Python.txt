
//************************************

// Written By: Chintan Pathak
// This code show different plots created using matplotlib library

//************************************

from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.001)

# Line Graph
plt.plot(x, norm.pdf(x))
plt.show()

#Multiple plot in one graph
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.show()

plt.savefig('/path/MyPlot.png', format='png')


#Adjust the axes

axes = plt.axes()
axes.set_xlim([-5, 5])
axes.set_ylim([0, 1.0])
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.show()
#Like wise you can add label, change color of line etc..


#Pie Chart

plt.rcdefaults()

values = [12, 55, 4, 32, 14]
colors = ['r', 'g', 'b', 'c', 'm']
explode = [0, 0, 0.2, 0.1, 0]
labels = ['India', 'United States', 'France', 'China', 'Europe']
plt.pie(values, colors= colors, labels=labels, explode = explode)
plt.title('Student Locations')
plt.show()


#Bar Chart

values = [12, 55, 4, 32, 14]
colors = ['r', 'g', 'b', 'c', 'm']
plt.bar(range(0,5), values, color= colors)
plt.show()

Scatter Plot
from pylab import randn

X = randn(500)
Y = randn(500)
plt.scatter(X,Y)
plt.show()


#Histogram
incomes = np.random.normal(27000, 15000, 10000)
plt.hist(incomes, 50)
plt.show()

#Box Plot
uniformSkewed = np.random.rand(100) * 100 - 40
high_outliers = np.random.rand(10) * 50 + 100
low_outliers = np.random.rand(10) * -50 - 100
data = np.concatenate((uniformSkewed, high_outliers, low_outliers))
plt.boxplot(data)
plt.show()






