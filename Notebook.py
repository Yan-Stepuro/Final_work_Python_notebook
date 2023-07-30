# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента

import json
import datetime

filename = "notes.txt"

# def start():
#     data = {}
#     data['notes'] = []
#     with open(filename, 'w') as outfile:
#         json.dump(data, outfile)
#     return 

def read_file(filename): 
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data

def write_file(filename, data):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

def add_note(filename):
    data = read_file(filename)
    current_datetime = datetime.datetime.now()

    data['notes'].append({
        'id': calc_id(filename),
        'head': input('Название заметки: '),
        'note': input('Текст заметки: '),
        'created': f"{current_datetime.date()}" + ' ' + f"{current_datetime.hour}" + ":" + f"{current_datetime.minute}",
        'last_modified': f"{current_datetime.date()}" + ' ' + f"{current_datetime.hour}" + ":" + f"{current_datetime.minute}",
    })
    write_file(filename, data)

def calc_id(filename):
    data = read_file(filename)
    max_id = 0
    for i in data['notes']:
        if max_id < int(i['id']):
            max_id = int(i['id'])
    next_id = max_id + 1

    return next_id

def change_note(filename):
    show_all_notes(filename)
    input_id = int(input('Введите id заметки для редактирования: '))
    new_head = input('Название заметки: ')
    new_note = input('Текст заметки: ')
    current_datetime = datetime.datetime.now()

    data = read_file(filename)

    for i in data['notes']:
        if input_id == i['id']:
            i['head'] = new_head
            i['note'] = new_note
            i['last_modified'] = f"{current_datetime.date()}" + ' ' + f"{current_datetime.hour}" + ":" + f"{current_datetime.minute}"
    write_file(filename, data)

def delete_note(filename):
    show_all_notes(filename)
    input_id = int(input('Введите id заметки, которую нужно удалить: '))
    data = read_file(filename)

    index_count = 0
    for i in data['notes']:
        if input_id == i['id']:
            del data['notes'][index_count]
        index_count += 1
    write_file(filename, data)

def show_all_notes(filename):
    data = read_file(filename)
    for i in data['notes']:
        print('Id: ' + str(i['id']))
        print('Head: ' + i['head'])
        print('Note: ' + i['note'])
        print('Created: ' + i['created'])
        print('Last modified: ' + i['last_modified'])
        print('')

# add_note(filename)
# change_note(filename)
# delete_note(filename)
# show_all_notes(filename)

def menu():
    print('Добро пожаловать в заметки!')

    while True:
        print('1 - Показать все заметки')
        print('2 - Добавить заметку')
        print('3 - Изменить заметку')
        print('4 - Удалить заметку')
        print('0 - Закрыть заметки')
        user_operation = int(input('Введите пункт меню: '))

        if user_operation == 1:
            show_all_notes(filename)
            continue
        elif user_operation == 2: 
            add_note(filename)
            continue
        elif user_operation == 3:
            change_note(filename)
            continue
        elif user_operation == 4:
            delete_note(filename)
            continue
        elif user_operation == 0:
            break

menu()