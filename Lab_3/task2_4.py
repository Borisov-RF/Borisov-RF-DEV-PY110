import json


def task():
    filename = "input.json"
    # TODO считать содержимое JSON файла
    with open(filename) as f:
        json_data = json.load(f)

    # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    gen_exr =(item["contains_improvement_appeals"] for item in json_data)
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
