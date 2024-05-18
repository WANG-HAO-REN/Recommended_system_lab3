import numpy as np
import matplotlib.pyplot as plt
from math  import pi

x = np.arange(0, 4*pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure()
plt.plot(x,y_sin, label="sin(x)")
plt.plot(x,y_cos, label="cos(x)")

plt.title("Plot of sin and cos from 0 to 4pi")
plt.xlabel("x values from 0 to 4pi")
plt.ylabel("sin(x) and cos(x) ")

plt.legend(loc="upper right")
plt.show()