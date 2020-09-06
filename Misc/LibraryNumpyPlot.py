import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

x=[[1,2,3],[4,5,6],[7,8,9]]
a=np.array(x)
print(a)


a=np.linspace(0,10,100)
b=a**2
plt.plot(a,b)