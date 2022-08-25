# ------------------------------- #
# Title: Assignment07
# Dev: RSar
# Desc: Start
# ChangeLog: (date,name,change)
#            2022/08/23, RSar, Created module to complete Assignment
# ------------------------------- #
import pickle
import datetime

# Data ----------------------------------------------------------- #
# Declare variables and constants
program_title_str = 'VIP Birthdays v1.0'
default_file_str = 'AppData.dat'
check_save_flag = [1]  # If = 1, then data saved/no changes, if = 0, changes \
# not saved
vip_lst = []

# Processing  ---------------------------------------------------- #

def read_data_from_file(working_file_str):
    try:
        file_obj = open(working_file_str, 'rb')
    except FileNotFoundError:
        print('\nERROR: File not found.')
    else:
        try:
            list_of_rows = pickle.load(file_obj)
        except EOFError:
            pass
        else:
            file_obj.close()
            return list_of_rows


def add_data_to_list(name, circle, dob, list_of_rows):
    row_dic = {"Name": str(name).strip(),
               "Circle": str(circle).strip(),
               "Birthday": str(dob).strip()}
    list_of_rows.append(row_dic)
    return list_of_rows, 0


def write_data_to_file(working_file_str, list_of_rows):
    file_obj = open(working_file_str, 'wb')
    pickle.dump(list_of_rows, file_obj)
    check_save_flag[0] = 1
    print('Data saved.')
    file_obj.close()


# Presentation (Input/Output)  ----------------------------------- #

def input_menu_choice():
    choice = str(input('Select option [1 to 3]: \t\t\t| ')).strip()
    return choice


def input_vip_name():
    while True:
        name = str(input('Enter name: \t\t\t\t\t\t| '))
        if len(name) < 1:
            print("\nERROR: Name cannot be blank.")
        else:
            return name


def input_vip_circle():
    print('''
\t*********************************
\tRelationship
\t---------------------------------
\t1 - Family
\t2 - Friend
\t3 - Business
\t4 - Other
\t*********************************''')
    circle = None
    while circle not in range(1, 5):
        try:
            circle = int(input('\nSpecify relationship [1-4]: \t\t| '))
            if circle in range(1, 5):
                return circle
            else:
                print('\nERROR: Invalid option selected. Choose number '
                      'from list.')
        except ValueError:
            print('\nERROR: Non-numeric value entered. Choose number from '
                  'list.')


def input_vip_dob():
    while True:
        dob = str(input('Enter birthday (yyyy-m-d): \t\t\t| '))
        try:
            datetime.datetime.strptime(dob, '%Y-%m-%d')
        except ValueError:
            print('\nERROR: Invalid date. Date should be in yyyy-m-d '
                  'format.')
        else:
            return dob


def output_menu():
    print('''
=====================================
MAIN MENU
=====================================

\t*********************************
\tOptions
\t---------------------------------
\t1 - Add a new VIP
\t2 - Save data to file  
\t3 - Exit program
\t*********************************
''')


def output_current_vip_in_list(list_of_rows):
    print('''\n\t*********************************
\tCurrent VIPs
\t---------------------------------
\tName \t\tBirthday
\t\t\t(yyyy-m-d)
\t---------------------------------''')

    for row in list_of_rows:
        print('\n\t' + row["Name"] +
              '\t\t' + row["Birthday"],
              end='')

    print('\n\t*********************************')


def output_vip_added():
    print('\n\t*********************************'
          '\n\tNew VIP added'
          '\n\t---------------------------------'
          '\n\tName: \t\t\t' + _name +
          '\n\tRelationship: \t' + c +
          '\n\tBirthday: \t\t' + _dob +
          '\n\t*********************************')


def output_exit_program():
    print("\n\tByeeee!")
    input("\n[Press ENTER key to quit.]")


# Main Body of Script  ------------------------------------------- #
print('\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'
      '\\\\\\\\\\\\\\\\' +
      '\nWelcome to ' + program_title_str + '!' +
      '\n/////////////////////////////////////')  # Display program name

print('\n\tOpening file: ' + default_file_str + '...')
# Step 1 - When the program starts, Load file.

vip_lst = read_data_from_file(working_file_str=default_file_str)

# Step 2 - Display a menu of choices to the user
while True:

    print('''
=====================================
DISPLAY DATA
=====================================''')

    # Step 3 Show current data
    output_current_vip_in_list(list_of_rows=vip_lst)
    output_menu()
    choice_str = input_menu_choice()

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Task
        print('''
=====================================
DATA ENTRY: Add new VIP
=====================================
''')
        _name = input_vip_name()

        _circle = input_vip_circle()
        if _circle == 1:
            c = 'Family'
        elif _circle == 2:
            c = 'Friend'
        elif _circle == 3:
            c = 'Business'
        elif _circle == 4:
            c = 'Other'

        _dob = input_vip_dob()

        output_vip_added()

        vip_lst, check_save_flag[0] = add_data_to_list(name=_name,
                                                       circle=_circle,
                                                       dob=_dob,
                                                       list_of_rows=vip_lst)
        continue

    elif choice_str.strip() == '2':  # Save Data to File
        if check_save_flag[0] == 0:
            write_data_to_file(working_file_str=default_file_str,
                               list_of_rows=vip_lst)
        else:
            print('\nALERT: No changes detected.')
        continue  # to show the menu

    elif choice_str.strip() == '3':  # Exit Program
        if check_save_flag[0] == 0:
            check_save = str(input('''
WARNING: You have unsaved changes. 
If you quit, your changes will not be saved.
        
Are you sure you want to quit? (Y/N): \t| '''))
            if check_save.lower() == 'n':
                continue

            elif check_save.lower() == 'y':
                output_exit_program()
                break

        elif check_save_flag[0] == 1:
            output_exit_program()
            break  # exit Menu loop
