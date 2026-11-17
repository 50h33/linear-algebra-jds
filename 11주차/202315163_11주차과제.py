import numpy as np

np.set_printoptions(precision=4, suppress=True, floatmode="fixed")


# 실습 7-1: 행렬 A의 특성다항식과 고유값
print("===== 실습 7-1 =====")
A = np.array([
    [2, 3],
    [3, -6]
], dtype=float)

# MATLAB의 poly(A), eig(A)에 해당
coefficients = np.poly(A)
eigenvalues = np.linalg.eigvals(A)
eigenvalues = np.sort(eigenvalues)

print("특성다항식의 계수 =")
print(coefficients)
print("고유값 =")
print(eigenvalues)
print()


# 실습 7-2: 행렬 A의 고유값과 고유벡터
print("===== 실습 7-2 =====")
A = np.array([
    [3, 2],
    [3, -2]
], dtype=float)

# MATLAB의 [X, lambda] = eig(A)에 해당
# np.linalg.eig(A)는 고유값을 먼저, 고유벡터를 나중에 반환
# 고유벡터는 X의 각 열에 저장됨
eigenvalues, X = np.linalg.eig(A)
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
X = X[:, order]
lambda_matrix = np.diag(eigenvalues)

print("X =")
print(X)
print("lambda =")
print(lambda_matrix)
print()


# 실습 7-3: 행렬 A의 고유값과 고유벡터
print("===== 실습 7-3 =====")
A = np.array([
    [3, -1, -1],
    [-12, 0, 5],
    [4, -2, -1]
], dtype=float)

# 고유값과 고유벡터 계산 (강의자료 38쪽의 파이썬 예시)
eigenvalues, X = np.linalg.eig(A)

# MATLAB 화면처럼 고유값을 2, 1, -1 순서로 정렬
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
X = X[:, order]

# 고유값을 대각행렬로 변환
lambda_matrix = np.diag(eigenvalues)

print("X =")
print(X)
print("lambda =")
print(lambda_matrix)
print()


# 실습 7-4: 행렬 A, B의 고유값
print("===== 실습 7-4 =====")
A = np.array([
    [0, 0, 0],
    [0, 2, 5],
    [0, 0, -1]
], dtype=float)

B = np.array([
    [4, 0, 0],
    [0, 0, 0],
    [1, 0, -3]
], dtype=float)

# MATLAB의 eig(A), eig(B)에 해당
eigenvalues_A = np.linalg.eigvals(A)
eigenvalues_B = np.linalg.eigvals(B)

print("A의 고유값 =")
print(eigenvalues_A)
print("B의 고유값 =")
print(eigenvalues_B)
