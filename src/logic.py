import sympy as sp
import numpy as np
import re

def add_matrices(matrices):
    def add_two(A, B):
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Matrices cannot be added: Incompatible dimensions.")
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    
    if len(matrices) < 2:
        raise ValueError("Addition requires at least 2 matrices")

    result = matrices[0]
    for matrix in matrices[1:]:
        result = add_two(result, matrix)
    return result

def subtract_matrices(matrices):
    def subtract_two(A, B): 
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Matrices cannot be subtracted: Incompatible dimensions.")
        return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    
    if len(matrices) < 2:
        raise ValueError("Subtraction requires at least 2 matrices")
            
    result = matrices[0]
    for matrix in matrices[1:]:
        result = subtract_two(result, matrix)
    return result

def multiply_matrices(matrices):
    def multiply_two(A, B):
        if len(A[0]) != len(B):
            raise ValueError("Matrices cannot be multiplied: Incompatible dimensions.")
        return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    
    if len(matrices) < 2:
        raise ValueError("Multiplication requires at least 2 matrices")

    result = matrices[0]
    for matrix in matrices[1:]:
        result = multiply_two(result, matrix)
    return result

def elementwise_multiply(matrices):
    def multiply_two(A, B):
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Matrices must have the same dimensions for element-wise multiplication")
        return [[A[i][j] * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    if len(matrices) < 2:
        raise ValueError("Element-wise multiplication requires at least 2 matrices")

    result = matrices[0]
    for matrix in matrices[1:]:
        result = multiply_two(result, matrix)
    return result

def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Determinant can only be computed for square matrices.")
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for c in range(len(matrix[0])):
        submatrix = [row[:c] + row[c + 1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(submatrix)
    return det

def inverse(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Inverse is only defined for square matrices.")

    def get_minor(m, row, col):
        return [r[:col] + r[col + 1:] for r in (m[:row] + m[row + 1:])]

    def compute_cofactor_matrix(m):
        return [[((-1) ** (i + j)) * determinant(get_minor(m, i, j)) for j in range(len(m))] for i in range(len(m))]

    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")

    cofactor_matrix = compute_cofactor_matrix(matrix)
    adjugate_matrix = transpose(cofactor_matrix)
    return [[adjugate_matrix[i][j] / det for j in range(len(matrix))] for i in range(len(matrix))]

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def trace(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Trace is only defined for square matrices.")
    return sum(matrix[i][i] for i in range(len(matrix)))

def eigenvalues(matrix):
    try:
        sym_matrix = sp.Matrix(matrix)
        eigenvals = sym_matrix.eigenvals()
        result_text = "Eigenvalues:\n"
        for eigenval, multiplicity in eigenvals.items():
            try:
                val = complex(eigenval)
                if val.imag == 0:
                    formatted_val = f"{val.real:.4f}"
                else:
                    formatted_val = f"{val.real:.4f} + {val.imag:.4f}i"
            except:
                formatted_val = str(eigenval)

            result_text += f"  λ = {formatted_val} (multiplicity: {multiplicity})\n"
        return result_text
    except Exception as e:
        raise ValueError(f"Error computing eigenvalues: {str(e)}")

def eigenvectors(matrix):
    try:
        sym_matrix = sp.Matrix(matrix)
        eigenvects = sym_matrix.eigenvects()
        result_text = "Eigenvectors:\n"
        
        for i, (eigenval, multiplicity, vectors) in enumerate(eigenvects):
            try:
                val = complex(eigenval)
                if val.imag == 0:
                    formatted_val = f"{val.real:.4f}"
                else:
                    formatted_val = f"{val.real:.4f} + {val.imag:.4f}i"
            except:
                formatted_val = str(eigenval)
            
            result_text += f"\nFor eigenvalue λ = {formatted_val}:\n"
            
            for j, vector in enumerate(vectors):
                result_text += f"  Eigenvector {j+1}: ["
                vector_components = []
                for component in vector:
                    try:
                        comp = complex(component)
                        if comp.imag == 0:
                            vector_components.append(f"{comp.real:.4f}")
                        else:
                            vector_components.append(f"{comp.real:.4f} + {comp.imag:.4f}i")
                    except:
                        vector_components.append(str(component))
                
                result_text += ", ".join(vector_components) + "]\n"
        return result_text
    except Exception as e:
        raise ValueError(f"Error computing eigenvectors: {str(e)}")

def characteristics(matrix):
    tr = transpose(matrix)
    is_symmetric = all(matrix[i][j] == tr[i][j] 
                      for i in range(len(matrix)) 
                      for j in range(len(matrix[0])))
    
    skew_tr = [[-matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    is_skew_symmetric = all(matrix[i][j] == skew_tr[i][j] 
                           for i in range(len(matrix)) 
                           for j in range(len(matrix[0])))
    
    is_diagonal = all(matrix[i][j] == 0 for i in range(len(matrix)) for j in range(len(matrix)) if i != j)
    is_upper_triangular = all(matrix[i][j] == 0 for i in range(len(matrix)) for j in range(i))
    is_lower_triangular = all(matrix[i][j] == 0 for i in range(len(matrix)) for j in range(i + 1, len(matrix)))
    
    return {
        "symmetric": is_symmetric,
        "skew_symmetric": is_skew_symmetric,
        "diagonal": is_diagonal,
        "upper_triangular": is_upper_triangular,
        "lower_triangular": is_lower_triangular
    }

def matrix_power(matrix, power):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix exponentiation is only defined for square matrices.")

    def multiply_two(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

    if power == 0:
        return [[1 if i == j else 0 for j in range(len(matrix))] for i in range(len(matrix))]
    if power == 1:
        return matrix
    
    result = matrix
    for _ in range(power - 1):
        result = multiply_two(result, matrix)
    return result

def scalar_multiply(matrix, scalar):
    return [[element * scalar for element in row] for row in matrix]

def gauss_transformation(M):
    A = np.array(M, dtype=float)
    n, m = A.shape

    for j in range(min(n, m)):
        pivot_row = j + np.argmax(np.abs(A[j:, j]))
        if abs(A[pivot_row, j]) < 1e-12:
            continue 

        if pivot_row != j:
            A[[j, pivot_row]] = A[[pivot_row, j]]

        for i in range(j + 1, n):
            factor = A[i, j] / A[j, j]
            A[i, j:] -= factor * A[j, j:]
            A[i, j] = 0.0

    return A.tolist()
