import matplotlib
# Make sure that we are using QT5
# matplotlib.use('Qt5Agg')
matplotlib.use('GTKAgg')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

print(plt.style.available)
# [u'dark_background', u'bmh', u'grayscale', u'ggplot', u'fivethirtyeight']
plt.style.use('presentation')
plt.figure(facecolor="white")
plt.plot(x, y, 'r') # 'r' is the color red
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('String Title Here')
plt.show()