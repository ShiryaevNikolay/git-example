def inputTargetVerteces():
    """
    Обрабатывает пользовательский ввод стартовой и конечной вершины
    """
    # Флаг для выхода из цикла. Сигнализирует, что данные введены верно/неверно
    correct_data = False
    while not correct_data:
        # Пользовательский ввод
        input_target_verteces = input("Ввердите стартовую вершину и конечную вершину в формате \"a b\": ")
        # Пытаемся получить массив вершин
        verteces = input_target_verteces.split(" ")
        # Если массив больше 2, то предлагаем пользователю еще раз ввести данные
        if len(verteces) != 2:
            continue

        try:
            start_vertex = int(verteces[0])
        except:
            print("Стартовая вершина введена некорректно. Попробуйте еще раз")
            continue
        try:
            end_vertex = int(verteces[1])
        except:
            print("Конечная вершина введена некорректно. Попробуйте еще раз")
            continue

        correct_data = True
    return str(start_vertex), str(end_vertex)
