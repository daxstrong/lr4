num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

average_arithmetic = (abs(num1) + abs(num2)) / 2

average_geometric = (abs(num1) * abs(num2)) ** 0.5

print(f"Среднее арифметическое: {average_arithmetic}")
print(f"Среднее геометрическое: {average_geometric}")
