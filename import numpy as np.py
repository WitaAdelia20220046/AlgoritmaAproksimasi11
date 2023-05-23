import numpy as np
from scipy.optimize import linprog

# Membentuk sistem persamaan linier dengan numpy
A = np.array([[1, 1], [-1, 2], [2, 1]])
b = np.array([6, 2, 5])
c = np.array([1, -2])

# Menyelesaikan sistem persamaan linier menggunakan algoritma simplex
res = linprog(c, A_ub=A, b_ub=b, method='simplex')

print('Nilai minimum fungsi tujuan:', res.fun)
print('Nilai variabel x:', res.x)
