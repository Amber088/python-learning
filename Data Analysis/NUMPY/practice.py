import numpy as np

age = np.array([20,30,40])
normalized = (age-age.min())/(age.max()- age.min())
print(normalized)
   