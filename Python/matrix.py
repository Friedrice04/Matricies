import numpy as np

a = np.array([[1, 5, 7],
              [5, 9, 5],
              [0, 2, 6]])

b = np.array([[6, 5, 2],
              [2, 8, 5],
              [9, 1, 9]])

Addarray = np.add(a, b)
MultArray = np.multiply(a, b)
divideArray = np.divide(a, b)
detA = np.linalg.det(a)
detB = np.linalg.det(b)

print(detA)
print(detB)
print(MultArray)
print(divideArray)
print(Addarray)
