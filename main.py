print(f"Task 1")
a = 1
b = 1.1
c = "Привет Мир!"
d = True
newprint = print
newprint(f"{a}, {b} и {c} сидели на трубе. Вот и {d}")
print(f"Task 2")
# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
user_seconds = int(input("Введите пожалуйста время в секундах : "))
user_seconds_hours = user_seconds // 3600
user_seconds = user_seconds % 3600
user_seconds_minutes = user_seconds // 60
user_seconds = user_seconds % 60
print(f"Вы ввели чч:мм:сс - {user_seconds_hours}:{user_seconds_minutes}:{user_seconds}")
print(f"Task 3")
# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
chislo_n = input("Введите число N: ")
print(f"Сумма чисел - {int(chislo_n) + int(chislo_n*2) + int(chislo_n*3)}")
print(f"Task 4")
# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
chislo = input("Введите число : ")
print(f"Самая большая цифра в числе - {max([int(x) for x in chislo])}")
