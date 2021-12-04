class Cell:

    def __init__(self, cell_count):
        self.cell_count = cell_count
        self.simbol = '*'

    def __add__(self, other):
        return f"сумма клеток равна{self.cell_count + other.cell_count}"


    def __sub__(self, other):
        if self.cell_count - other.cell_count < 0:
            return "Ошибка. Количество первых клеток меньше вторых"
        else:
            return f"Разность клеток равна{self.cell_count + other.cell_count}"

    def __mul__(self, other):
        return f"Число ячеек в общей клетке: {self.cell_count * other.cell_count}"

    def __truediv__(self, other):
        return f"Число ячеек в общей клетке: {self.cell_count / other.cell_count}"

    def make_order(self, count):
        x = self.cell_count
        while x > 0:
            for k in range(1, count + 1):
                print(self.simbol, end='')
                x -= 1
                if x <= 0:
                    break
            print('\n', end='')

a = Cell(10)
b = Cell(2)

print(a + b)
print(a - b)
print(a * b)
print(a / b)

a.make_order(4)
b.make_order(2)
