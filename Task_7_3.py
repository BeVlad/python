class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'({self.quantity})'

    def __add__(self, other):
        return f'Sum of cells: {str(Cell(self.quantity + other.quantity))}'

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return f'Cell difference: {Cell(int(self.quantity - other.quantity))}'
        return f'Negative difference. Operation cannot be performed.'

    def __mul__(self, other):
        return f'Cell multiplication: {Cell(int(self.quantity * other.quantity))}'

    def __truediv__(self, other):
        return f'Cell division: {Cell(round(self.quantity // other.quantity))}'

    def make_order(self, cells_count):
        row = ''
        for _ in range(int(self.quantity / cells_count)):
            row += f'{"*" * cells_count}\\n '
        row += f'{"*" * (self.quantity % cells_count)}'
        return row


print("Creating Cell Objects")
cell1 = Cell(10)
cell2 = Cell(15)

cell3 = Cell(30)
cell4 = Cell(45)

print()

print("Folding")
print(cell1 + cell2)

print()

print("Subtraction")
print(cell2 - cell1)
print(cell4 - cell3)

print()

print("Multiplication")
print(cell2 * cell1)

print()

print("Division")
print(cell1 / cell2)

print()

print("Organizing cells by row")
print(cell1.make_order(5))
print(cell2.make_order(10))