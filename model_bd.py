db_list = []

def read_db(path: str) -> list:
    global db_list
    with open(path, 'r', encoding= 'UTF-8') as file:
        my_list = file.readlines()
        for line in my_list:
            id_dict = dict()
            line = line.strip().split(';')
            id_dict['lastname'] = line[0]
            id_dict['firsname'] = line[1]
            id_dict['phone'] = line[2]
            id_dict['comment'] = line[3]
            db_list.append(id_dict)


def save_db(path: str) -> list:
    global db_list
    with open(path, 'w', encoding= 'UTF-8') as file:
        for i in range(len(db_list)):
            for value in db_list[i].values():
                file.write(value + ';')
            if i < len(db_list) - 1:
                 file.write('\n')
            