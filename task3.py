def my_func():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = float(input("Введите третье число: "))
    d = [a, b, c]
    d.sort()
    d = d[1] + d[2]
    print(d)
my_func()