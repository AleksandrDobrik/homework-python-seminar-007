import model_bd 
import view

path = 'text.txt'


def input_handler(inp: int):
    match  inp:
        case 1: 
            view.show_all(model_bd.db_list)
        case 2:
            model_bd.read_db(path)
            view.db_success(model_bd.db_list)
        case 3:
            model_bd.save_db(path)
        case 4:
            model_bd.db_list.append(view.create_contact()) 
        case 5:
            view.change_contact(model_bd.db_list)
        case 6:
            view.delete_contact(model_bd.db_list)
        case 7:
            view.search_contact(model_bd.db_list)        
        case 8:
            view.exit_program()

def start():
    while True:           
        user_inp =  view.main_menu()
        input_handler(user_inp)