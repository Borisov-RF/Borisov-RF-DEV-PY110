def task(numbers: list) -> int:
    gen_exp = ...  # TODO записать выражение-генератор для возведения чисел в квадрат
    #return sum(gen_exp)
    return sum(pow(x, 2) for x in numbers)


if __name__ == "__main__":
    list_numbers = [i for i in range(1, 11)]  # list(range(1, 11))
    print(task(list_numbers))
