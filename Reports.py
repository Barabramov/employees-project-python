from Employees_Project import *
import pandas as pd
from datetime import time

def employee_report():
    the_id_after_checking = checking_if_id_already_exist_in_the_system(input, "\nEnter your employee ID- ")
    if the_id_after_checking[0] is False:
        print(error_style("The ID-"), the_id_after_checking[1], error_style(" not exist in the system. "))
    else:

        df_attendance = open_attendance_log_file()[open_attendance_log_file()["EMPLOYEE ID"] == the_id_after_checking[1]]
        print(pd.DataFrame(df_attendance.set_index("EMPLOYEE ID")))
    back_to_menu()


def month_report():
    df_attendance = open_attendance_log_file().sort_values(by="DATE", ascending=True).set_index("DATE").last("M")
    print(pd.DataFrame(df_attendance, index=None))
    back_to_menu()


def late_emp():
    x = pd.to_datetime(open_attendance_log_file()['TIME'])
    print(open_attendance_log_file().loc[x.dt.time > time(9, 30)])
    back_to_menu()

