def main_menu():
    print('Главное меню')
    menu_list = [
        'Показать все контакты',
        'Открыть фаил',
        'Сохранить фаил',
        'Создать контакт',
        'Изменить контакт',
        'Удалить контакт',
        'Поиск контактов',
        'Выход'
    ]
    for i in range(len(menu_list)):
        print(f'    {i + 1}. {menu_list[i]} ')
    user_input = int(input('Введите команду :> '))
    # сделать валидацию
    return user_input

def show_all(db: list):
    if db_success(db):
        for i in range(len(db)):
            contakt_id = i + 1 
            print('\t',contakt_id, end = '. ')
            for v in db[i].values():
                print(f' {v}', end = ' ')
            print()

def db_success(db: list):
    if db:
        print('Телефонная книга открыта ')
        return True
    else:
        print('Телефонная книга пустая или не открыта')
        return False

def exit_program():
    print('Завершение программы.')
    exit()

def create_contact():
    print('Создание нового контакта ')
    new_contact = dict()

    new_contact['lastname'] = input('Введите фамилию >:')
    new_contact['firsname'] = input('Введите имя >:')
    new_contact['phone'] = input('Введите телефон >:')
    new_contact['comment'] = input('Введите коментарий >:')
    return new_contact

def search_contact(db: list):
    search_str = input('Поиск контакта :> ')
    search_list = []

    for item in db:
        for value in item.values():
            if value.find(search_str) != -1:
                search_list.append(item)
                break

    if len(search_list) == 0:
        print('\t Совпадений не найдено')
    else:
        for i in range(len(search_list)):
            id_contact = i + 1
            print('\t',id_contact, end = '. ')
            for j in search_list[i].values():
                print(f' {j}', end = ' ')
            print()

def delete_contact(db: list):
    print('Удаление контакта ')
    id_contact = int(input('\t Введите ID контакта который хотите удалить :> '))
    

    if 0 <= id_contact <= len(db):
        print(db[id_contact])
        end = input('Вы хотите удалить этот контакт? 1- да 2 - нет ')
        if end == '1':
            db.pop(id_contact - 1)
    else:
        print('Контакта с таким ID не существует')



def change_contact(db: list):
    print('Изменение контакта ')
    while True:
        id_contact = int(input('\t Введите ID контакта который хотите изменить :> '))

        if 0 <= id_contact <= len(db):
            for i in db[id_contact - 1].values():
                print(i, end = ' ')
            print()

            end = input('Выбран нужный контакт? 1 - Да 2 - Нет ')
            if end == '2':
                break

            while True:
                i = 0
                for key in db[id_contact - 1].keys():
                    i += 1
                    print(f'{i} {key}', end = ' ')
                print()

                id_value = int(input('\t Введите ID поля которое хотите изменить :> '))
                value = input('\t Введите новые данные для поля :> ')

                i = 0
                for key in db[id_contact - 1].keys():
                    i += 1
                    if i == id_value:
                        db[id_contact - 1][key] = value 
                
                end = input('Вы хотите поменять други поля? 1 - Да 2 - Нет ')
                if end == '2':
                    break                                 
        else:
            end = input('\t Контакта с таким ID не существует. Хотите продолжить? 1 -> Да 2 -> Нет ')
        
        if end == '2':
             break
        

            



