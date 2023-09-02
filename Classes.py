from Employees_Project import *
import pandas as pd



class Employees(object):
    def __init__(self, employee_id, name, phone, age):
        self.employee_id = int(employee_id)
        self.name = str(name)
        self.age = int(age)
        self.phone = int(phone)

    def info(self):
        return pd.DataFrame({"EMPLOYEE ID": [int(self.employee_id)], "NAME": [str(self.name)], "PHONE": [int(self.phone)],
                             "AGE": [int(self.age)]})


def details_for_employees_class(id_num, name, phone, age, which_type):
    if which_type is None:
        users = Employees(employee_id=int(id_num), name=str(name), phone=int(phone), age=int(age))
        return users
    else:
        users = Employees(employee_id=int(id_num), name=str(which_type(name)), phone=exception_check(which_type, phone), age=exception_check(which_type, age))
        return users


class AttendanceLog():
    def __init__(self, employee_id, name, date, time):
        self.employee_id = employee_id
        self.name = name
        self.date = date
        self.time = time

    def info(self):
        return pd.DataFrame({"EMPLOYEE ID": [self.employee_id], "NAME": [self.name], "DATE": [self.date], "TIME": [self.time]})

def details_for_attendance_class(id_num, name, date, time):
    users = AttendanceLog(employee_id=int(id_num), name=str(name), date=date, time=time)
    return users



