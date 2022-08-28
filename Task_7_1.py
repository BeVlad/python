class Matrix:

    template_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __init__(self, matrix_list_1, matrix_list_2):
        self.matrix_list_1 = matrix_list_1
        self.matrix_list_2 = matrix_list_2

    def __str__(self):
        return str(
            '\n'.join([
                str('\t'.join([
                    str(self.template_matrix[a][b]) for b in range(len(self.template_matrix[a]))
                ])) for a in range(len(self.template_matrix))
            ])
        )

    def __add__(self):
        for a in range(len(self.matrix_list_1)):
            for b in range(len(self.matrix_list_2[a])):
                self.template_matrix[a][b] = self.matrix_list_1[a][b] + self.matrix_list_2[a][b]
        return self.__str__()


print(Matrix([[5, 18, 11], [6, 17, 23], [41, 30, 9]], [[5, 18, 11], [6, 17, 23], [41, 50, 9]]).__add__())