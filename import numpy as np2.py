import numpy as np
from scipy.optimize import linprog

# Membentuk sistem persamaan linier dengan numpy
A = np.array([[-3, -2, -4, 0], [-1, -4, 0, -3], [-2, -3, -5, -4]])
b = np.array([-15, -10, -20])
c = np.array([-10, -8, -15, 0])

# Menyelesaikan sistem persamaan linier menggunakan algoritma simplex
res = linprog(c, A_ub=A, b_ub=b, method='simplex')

print('Nilai maksimum fungsi tujuan:', -res.fun)
print('Nilai variabel x:', res.x)
