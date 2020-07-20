class Matrix:
    def __init__(self, matrix_input):
        self.data = matrix_input

    def __str__(self):
        for i in self.data:
            for j in i:
                print(j, end=' ')
            print('\n')
        return f''

    def __add__(self, matrix):
        matrix_sum = self.data
        try:
            for i in range(0, len(self.data)):
                for j in range(0, len(self.data[i])):
                    matrix_sum[i][j] += matrix.data[i][j]
            return Matrix(matrix_sum)
        except IndexError:
            print("Матрицы нельзя сложить!")
            exit(0)

matrix_1 = Matrix([[1, 2], [3, 4]])
matrix_2 = Matrix([[1, 2], [3, 4]])
print(matrix_1 + matrix_2)
