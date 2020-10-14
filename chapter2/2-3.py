import numpy as np
import numpy.random as random
import scipy.linalg as linalg
from scipy.optimize import minimize_scalar


matrix = np.array([[1,-1,-1], [-1,1,-1], [-1,-1,1]])
print(linalg.det(matrix))

matrix = np.array([[1,1,1], [-1,-1,-1], [-1,-1,-1]])
print(linalg.det(matrix))