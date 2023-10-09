example = "4 * 100 - 54"

correct_answer = 4 * 100 - 54

print(f"Решите математическую задачу: {example} = ?")

user_answer_str = input()

user_answer = int(user_answer_str)

print(f"Правильный ответ: {correct_answer}")
print(f"Ваш ответ: {user_answer}")

if user_answer == correct_answer:
    print("Ваш ответ верный!")
else:
    print("Извините, ваш ответ неверный.")