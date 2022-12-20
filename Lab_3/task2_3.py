import json


def task():
    filename = "input.json"
    # TODO считать содержимое JSON файла
    with open(filename) as f:
        json_data = json.load(f)

    # TODO найти максимальный элемент по ключу score
    return max(json_data, key=lambda i: i["score"])


if __name__ == "__main__":
    print(task())
