from Employees_Project import *
import pandas as pd

# my file = C:\Users\barab\Desktop\employees_file.xlsx


def checking_if_id_already_exist_in_the_system(which_type, id_num):
    df_employees_file = open_main_employees_file()
    user_id = exception_check(which_type, id_num)
    if user_id in list(df_employees_file["EMPLOYEE ID"]):
        return [True, user_id]
    else:
        return [False, user_id]


def open_main_employees_file():
    return pd.read_excel(r'C:\Users\barab\Desktop\employees.xlsx')


def open_attendance_log_file():
    while True:
        try:
            return pd.read_excel(r'C:\Users\barab\Desktop\attendance_log.xlsx')
        except ValueError:
            print(error_style("The file is empty"))
            continue


def read_file(file):
    while True:
        try:
            return pd.read_excel(input(file), header=None)

        except FileNotFoundError:
            print(error_style("File does not exist\n please try again. "))
        continue


def exception_check(which_type, checking) -> int or ValueError:
    while True:
        if which_type is None:
            x = checking
        else:
            x = which_type(checking)
        try:
            h = int(x)
            return h
        except ValueError:
            print(error_style("***** This is not a number. Please enter a valid number ****"))
            continue



def save_data_in_files(file, route, data):
    writer = pd.ExcelWriter(route, engine='xlsxwriter')
    new = pd.concat([file, data.info()], ignore_index=True, join="inner")
    new.to_excel(writer, sheet_name='Sheet1', index=False, columns=data.info().keys())
    writer.save()

def emp_remove_data(df_employees_file, users, data_to_remove):
    df_employees_file = df_employees_file.drop(data_to_remove, axis=0)
    writer = pd.ExcelWriter(r'C:\Users\barab\Desktop\employees.xlsx', engine='xlsxwriter')
    df_employees_file.to_excel(writer, sheet_name='Sheet1', index=False, columns=users.info().keys())
    writer.save()




