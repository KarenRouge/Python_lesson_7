import copy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        str1 = ''
        for i in range(len(self.matrix)):
            str1 = str1 + '\t'.join(map(str, self.matrix[i])) + '\n'
        return str1

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        sum = copy.deepcopy(self.matrix)
        for a in range(len(self.matrix)):
            for b in range(len(self.matrix[a])):
                sum[a][b] = self.matrix[a][b] + other.matrix[a][b]
        return Matrix(sum)


matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_2 = [11, 12, 13], [14, 15, 16], [17, 18, 19]
ls1 = Matrix(matrix_1)
ls2 = Matrix(matrix_2)
print(ls1)
ls3 = ls1 + ls2
print(ls3)
print(type(ls3))
