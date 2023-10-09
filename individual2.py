a2a1 = int(input("Введите двузначное число: "))

b = int(input("Введите однозначное число: "))

a = a2a1 // 10  # Десятки
a1 = a2a1 % 10  # Единицы

result = a + b

result_a = result // 10
result_b = result % 10

print(f"Первая цифра результата: {result_a}")
print(f"Вторая цифра результата: {result_b}")
