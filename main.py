import main


class Matrix:
    def __init__(self, a, b, c):
        self.matrix = a
        self.rows = b
        self.columns = c

    def MatrixOutput(self) -> object:
        for item in self .matrix:
            print(item)

    def MatrixAddition(self, twoMatrix):
        for x in range(self.rows):
            for y in range(self.columns):
                self.matrix[x][y] = self.matrix[x][y] + twoMatrix.matrix[x][y]

    def Multiple(self, twoMatrix):
        A = main.deepcopy(self.matrix)
        for x in range(self.rows):
            for y in range(self.columns):
                A[x][y] = 0
        for x in range(self.rows):
            for y in range(twoMatrix.columns):
                for z in range(twoMatrix.rows):
                    A[x][y] += self.matrix[x][z] * twoMatrix.matrix[z][y]
        self.matrix = A

    def NumberMatrix(self, number):
        for x in range(self.rows):
            for y in range(self.columns):
                self.matrix[x][y] = self.matrix[x][y] * number


firstMatrix = Matrix([[45, 4], [10, 6]], 2, 2)
secondMatrix = Matrix([[0, 7], [3, 7]], 2, 2)
firstMatrix.MatrixAddition(secondMatrix)
firstMatrix.MatrixOutput()
firstMatrix = Matrix([[6, 7], [3, 1]], 2, 2)
firstMatrix.Multiple(secondMatrix)
firstMatrix.MatrixOutput()
firstMatrix = Matrix([[4, 12], [7, 8]], 2, 2)
firstMatrix.NumberMatrix(2)
firstMatrix.MatrixOutput()

