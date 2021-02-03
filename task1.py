def my_func():
    a = float(input("Введите число, которое будем делить: "))
    b = float(input("Введите делитель: "))
    if b==0:
        print("Невозможно деление на 0")
    else:
        c = a / b
        print("Ответ равен: ", c)
my_func()