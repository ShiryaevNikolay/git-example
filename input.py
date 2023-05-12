def inputTargetVerteces():
    correct_data = False
    while not correct_data:
        input_target_verteces = input("Ввердите стартовую вершину и конечную вершину в формате \"a b\": ")
        verteces = input_target_verteces.split(" ")
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
    return (start_vertex, end_vertex)
