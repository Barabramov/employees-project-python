from Employees_Project import *

def main() -> int or str:
    user = exception_check(input, (f" \n{Bcolors.CGREYBG} Please select the action you need:{Bcolors.ENDC}\n To add employee enter- 1,\n "
                             "To delete employee enter- 2,\n" " To mark attendance enter- 3."
                             " \n To the reports enter-4. \n\n you choose number: "))
    if user == 1:
        way_to_add = exception_check(input, (f" \n {Bcolors.CGREYBG}On which way do you want to add employee: {Bcolors.ENDC}\n To add employee manually "
                                       "enter- 1, \n To add employee from file enter- 2, \n\n you choose number: "))
        if way_to_add == 1:
            add_emp_manually()
        elif way_to_add == 2:
            add_emp_from_file()
        else:
            print(error_style(" Wrong number"))

    elif user == 2:
        del_emp_from_file()
    elif user == 3:
        mark_attendance()
    elif user == 4:
        which_report = exception_check(input, ("\n To attendance report of an employee enter- 1, \n"
                                        " To print a report for current month for all the employees enter- 2, \n"
                                        " To print an attendance report for all employees who were late enter- 3 \n"
                                        "\n you choose number: "))
        if which_report == 1:
            employee_report()
        elif which_report == 2:
            month_report()
        elif which_report == 3:
            late_emp()
        else:
            print(" Wrong number")
    else:
        print(" Wrong number")



def back_to_menu():
    x = exception_check(input, (f"\n {Bcolors.CSELECTED}Something more?{Bcolors.ENDC}\n Back to the main Menu enter- 1.\n To finish"
                        " enter- 2.\n you choose number- "))
    if x == 1:
        main()
    else:
        print(f"{Bcolors.OKGREEN} goodbye and Have a good day!{Bcolors.ENDC}")


if __name__ == '__main__':
    main()
else:
    pass




