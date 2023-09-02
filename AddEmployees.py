from Employees_Project import *



def add_emp_manually():
    number_of_users = exception_check(input, "\n Please enter the number of users: ")
    for user in range(number_of_users):
        the_id_after_checking = checking_if_id_already_exist_in_the_system(input, " Enter the ID number- ")
        if the_id_after_checking[0] is True:
            print(error_style("ID already exists in the system"))
        else:
            users = details_for_employees_class(the_id_after_checking[1], " Enter your name- ", " Enter your phone- ",
                                                " Enter your age- ", input)
            save_data_in_files(open_main_employees_file(), r'C:\Users\barab\Desktop\employees.xlsx', users)
    back_to_menu()


def add_emp_from_file():
    user_file_path = read_file("\n"r' Please enter the path where the Excel file is stored\File name.xlsx :  ')
    for id_num in list(user_file_path[0]):
        the_id_after_checking = checking_if_id_already_exist_in_the_system(None, id_num)
        if the_id_after_checking[0] is True:
            print(error_style("The ID-"), the_id_after_checking[1], error_style(" not saved because it already exist in the system. "))
            continue
        else:
            index_id_number = list(user_file_path[0]).index(the_id_after_checking[1])
            users = details_for_employees_class(the_id_after_checking[1], user_file_path[1][index_id_number],
                                                user_file_path[2][index_id_number], user_file_path[3][index_id_number], None)
            save_data_in_files(open_main_employees_file(), r'C:\Users\barab\Desktop\employees.xlsx', users)
    back_to_menu()
