def task() -> float:
    # Данные, которые дают сумму произведений, равную 2.296
    data = [
        {
            "score": 0.123,
            "weight": 1
        },
        {
            "score": 0.456,
            "weight": 2
        },
        {
            "score": 0.788,
            "weight": 1.6
        }
    ]

    # Инициализируем переменную для хранения суммы произведений
    total_sum = 0.0

    # Проходим по каждому словарю в списке
    for item in data:
        # Вычисляем произведение score и weight
        product = item.get("score", 0) * item.get("weight", 0)
        # Добавляем произведение к общей сумме
        total_sum += product

    # Округляем результат до 3 знаков после запятой
    return round(total_sum, 3)


# Вызов функции и вывод результата
result = task()
print(result)