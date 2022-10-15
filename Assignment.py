import numpy as np
a = np.array([[[1,0,2],[30,1,4]],[[0,0,0],[-1,2,1]],[[1,1,-2],[-1,0,2]]])
print(np.sort(a, axis=2,kind=None,order=None))
print(np.where(a==30))