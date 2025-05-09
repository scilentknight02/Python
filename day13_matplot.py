import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,100)
print(x)
print()
y = np.random.randint(1, 50, 100)
print(y)
plt.plot(x,y)
plt.show()