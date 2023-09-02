from Employees_Project import *


def del_emp_from_file():
    user_file_path = read_file("\n"r' Please enter the path where the Excel file is stored\File name.xlsx :  ')
    for id_num in list(user_file_path[0]):
        the_id_after_checking = checking_if_id_already_exist_in_the_system(None, id_num)
        if the_id_after_checking[0] is False:
            print(Employees_Project.error_style("The ID-"), the_id_after_checking[1], error_style(" not exist in the system. "))
            continue
        else:
            index_new_id = list(user_file_path[0]).index(the_id_after_checking[1])
            users = details_for_employees_class(the_id_after_checking[1], user_file_path[1][index_new_id], user_file_path[2][index_new_id],
                                                user_file_path[3][index_new_id], None)
            index_exist_id = open_main_employees_file()["EMPLOYEE ID"].index(the_id_after_checking[1])
            if (users.name == open_main_employees_file()["NAME"][index_exist_id]) and (users.phone == open_main_employees_file()["PHONE"][index_exist_id])\
                    and (users.age == open_main_employees_file()["AGE"][open_main_employees_file()]):
                emp_remove_data(open_main_employees_file(), users, index_exist_id)
            else:
                print(error_style("Not the same information in ID-"), the_id_after_checking[1])
    back_to_menu()




