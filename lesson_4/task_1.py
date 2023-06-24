# Напишите функцию для транспонирования матрицы


def transpone_matrix(matrix_in):
    matrix_in = [[matrix_in[j][i] for j in range(len(matrix_in))] for i in range(len(matrix_in[0]))]
    return matrix_in

    
matrix = [[2, 3, 4], [5, 6, 7]]    
print(f'{matrix}\n\n{transpone_matrix(matrix)}')