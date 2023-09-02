from datetime import datetime
from Employees_Project import *

def mark_attendance():
    the_id_after_checking = checking_if_id_already_exist_in_the_system(input, " Please enter your ID number- ")
    if the_id_after_checking[0] is False:
        print(error_style("The ID-"), the_id_after_checking[1], error_style(" not exist in the system. "))
    else:
        index_exist_id = list(open_main_employees_file()["EMPLOYEE ID"]).index(the_id_after_checking[1])
        users = details_for_attendance_class(the_id_after_checking[1], open_main_employees_file()["NAME"][index_exist_id],
                                             datetime.now().date(), datetime.now().time())
        save_data_in_files(open_attendance_log_file(), r'C:\Users\barab\Desktop\attendance_log.xlsx', users)
    back_to_menu()