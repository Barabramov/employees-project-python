from .Styling import Bcolors, error_style
from .Config import checking_if_id_already_exist_in_the_system, open_main_employees_file,\
    open_attendance_log_file, read_file, exception_check, save_data_in_files, emp_remove_data
from .AddEmployees import add_emp_manually, add_emp_from_file
from .Main import main, back_to_menu
from .Classes import Employees, details_for_employees_class, AttendanceLog, details_for_attendance_class
from .MarkAttendance import mark_attendance
from .Reports import employee_report, month_report, late_emp
from .RemoveEmployees import del_emp_from_file




