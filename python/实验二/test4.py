import numpy as np

A = np.mat("1 2 3; 4 5 6; 7 8 9")

eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"特征值为：\n{eigenvalues}\n和特征向量:\n{eigenvectors}")

U, Sigma, V = np.linalg.svd(A, full_matrices=False)
print(f"U:\n{U}\nSigma:\n{Sigma}\nV:\n{V}")

B = np.mat("4; 8; 2")
try:
    x = np.linalg.solve(A,B)
    print("解为\n",x)
except np.linalg.LinAlgError as e:
    print(e)



