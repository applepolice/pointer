import table_import

def table_work():
    markdown_data = ['Разделы', 'Оценка', 'Рекомендации', 'Приоритет']
    header_data = []
    header_points = []
    for i in range(table_import.headers_length()):
        header_data.insert(i, table_import.headers(i))
        header_points.insert(i, table_import.headers_points(i) / table_import.headers_maxpoints(i))

    data_dict = dict(zip(header_data, header_points))

    list_d = list(data_dict.items())
    # list_d.sort(key=lambda i: i[1])
    list_list = []
    for i in list_d:
        list_list.append(list(i))


    for i in list_list:
        if i[1] <= 0.3:
            i.insert(2,'Серьезные изменения')
        elif (i[1] > 0.3) and (i[1] <= 0.5):
            i.insert(2, 'Значительные изменения')
        elif (i[1] > 0.5) and (i[1] <= 0.7):
            i.insert(2, 'Средние изменения')
        elif (i[1] > 0.7) and (i[1] <= 0.9):
            i.insert(2, 'Небольшие изменения')
        elif i[1] > 0.9:
            i.insert(2, 'Мелкие изменения')

    for i in list_list:
        if i[1] <= 0.2:
            i.insert(3, 'Максимальный')
        elif (i[1] > 0.2) and (i[1] <= 0.5):
            i.insert(3, 'Высокий')
        elif (i[1] > 0.5) and (i[1] <= 0.8):
            i.insert(3, 'Средний')
        elif i[1] > 0.8:
            i.insert(3, 'Низкий')

    for i in list_list:
        i[1] = int(i[1]*100)
        i[1] = str(i[1]) + '/100'

    list_list.insert(0, markdown_data)

    #print(list_list)
    return(list_list)



table_work()


