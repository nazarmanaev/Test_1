import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Считываем содержимое CSV файла
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csv_file:
        # Используем csv.DictReader для автоматического создания словарей
        csv_reader = csv.DictReader(csv_file)

        # Преобразуем данные в список словарей
        data = [row for row in csv_reader]

    # Сериализуем данные в JSON и записываем в файл с отступами
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Выполняем задачу
    task()

    # Читаем и выводим содержимое JSON файла для проверки
    with open(OUTPUT_FILENAME, mode='r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")