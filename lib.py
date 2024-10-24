def calculator(num1, num2, operation):
    """
    Функция выполняет арифметические операции с двумя числами.

    :param num1: Первое число
    :param num2: Второе число
    :param operation: Операция (+, -, *, /)
    :return: Результат операции
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ValueError("Деление на ноль!")
        return num1 / num2
    else:
        raise ValueError("Неверная операция")
def bubble_sort(lst):
    """
    Функция сортирует список методом пузырьковой сортировки и возвращает отсортированную копию списка.

    :param lst: Список чисел
    :return: Отсортированный список
    """
    sorted_lst = lst.copy()
    for i in range(len(sorted_lst)):
        for j in range(0, len(sorted_lst) - i - 1):
            if sorted_lst[j] > sorted_lst[j + 1]:
                sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]
    return sorted_lst
def fibonacci(n):
    """
    Функция возвращает список из n чисел Фибоначчи.

    :param n: Количество чисел Фибоначчи для генерации
    :return: Список из n чисел Фибоначчи
    """
    if n <= 0:
        raise ValueError("n должно быть больше 0")
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence[:n]

