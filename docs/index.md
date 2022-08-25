# Python Script: VIP Birthdays
*RSar, 2022.08.24*


## Prologue

In support of the adage "Don't Let 'Perfect' Be the Enemy of 'Good' ", this GitHub page is an excerpt of the [A07-RSar copy.docx
](https://github.com/rsar-uw/IntroToProg-Python-Mod07/blob/9ccae2b2a1608882bb9ab6fbc0609516c9c320b3/A07-RSar%20copy.docx) (specifically, exceprts from Sections 2, 4, 5, and 6.2).

## Introduction

I have concerns about the time requirements for this week’s assignment. In addition to the ‘normal’ assignment requirements, there is also an additional aspect of self-learning that will be needed. I think that one value I have found from the references provided to us so far is the “short cut” in time needed to “wade through” the vast amount of information available. There is a great quantity and wide spectrum in quality of content “in the wild” after all: *The net is vast and infinite.*

Additionally, there have been unforeseen competing priorities that may manifest this weekend. So, to crash my own schedule (which, admittedly is less than ideal), my approach will be to learn this module’s lessons by starting with the assignment. Although I acknowledge that there are simpler (and still effective) ways to demonstrate one’s knowledge of this week’s content, I would like to try where practice, to both: simulate real-world time pressures / workloads and build upon the preceding weeks’ lessons. 

So far, it’s still been fun though.

## Module assignment

### Requirements

“Pickling + Exception handling" (Randall R., Assignment07_instructions.docx, Self-published, 2022).

Use case demos:
1.	Open file (file extension: .dat (binary))
2.	Add data
3.	Save (write data to binary file)
4.	Quit

### Design

This section includes the relevant components in the Python code that compose my proposed solution to the assignment.

#### Program description

Since the primary objective of this assignment is to demonstrate the requirements, I am building a “dummy” program as a base reference. The base reference program will be a birthday record keeper: “VIP Birthdays”.

The program will record: Name, Relationship (a.k.a. circle), and Date of Birth (a.k.a., dob).

#### Data structure

I have found it helpful to know before coding what is the expected data structure and data file output. As the output is going to a binary file (.dat) – where the raw data in the file is not human readable – I’m not going to output as a comma-separated values (CSV) file. Since viewing the data requires the program to do, I’ll leave the extract-transform-load (ETL) workload to the program.

```
Name: alphanumeric, free-text
	
Circle: mutually exclusive, pre-defined groups: Family | Friend | Business | Other
	
DOB: yyyy-m-d
```

Due to increased documentation requirements (e.g., publishing to GitHub webpage), I will deprioritize development to the minimum code required to demonstrate use cases specified (Section 4.1).
Where possible leverage existing code from prior assignment: A06-RSar.py

Since there is no base code to start from for this assignment, I am using the template I had created in the prior assignment to structure the code for each module (Figure 9).

#### Program architecture

Following lessons from Module06 (Randall R., Mod6PythonProgrammingNotes.docx, Self-published, 2019), efforts will be made to follow principles of abstraction and separation of concerns.

I have found it helpful to plan out in advance (at least at a high-level), how to organize requirements into features, and the order in which to develop components, integrate, and then iterate further.

Module: Add
1.	Manually create default output file
2.	Write data to default output file
3.	Verify data is being written (i.e., open default output file in text editor, note before / after changes)
4.	Input functions to allow user to enter data
5.	Exception catching

Module: Load
1.	Open default output file
2.	Read raw data from default output file
3.	Display data from default output file
4.	Exception catching

Module: Quit
1.	Exit program
2.	Check if changes to data have been saved before quitting
3.	Input functions to allow user to choose to quit without saving or return to menu

#### User journey flows

Understanding how the user is expected to navigate through the program further aids development.

Flow #0 – Core: User opens program > Program opens default file > Program loads data from default file into program memory > Program displays current data to user in human-readable format > Program displays menu of options / functions to user: Add data, Save data, Quit program

Flow #1 – Standard: User adds data > User saves data > User quits program

Flow #2 – Changes made + No save: User adds data > User quits program (without saving)
  * Quit program w/o change
  * Return user to menu

Flow #3 – No change + Save: User saves data (without making changes)
  * Return user to menu

#### Open file, Display data

*Requirement 1: Allow program to open default output file.*

*Requirement 2: Allow program to display current data to user in human-readable format.*

The program begins by importing the pickle module: import pickle, which is needed for using the pickle function to ‘load’ the data from the file.

The program begins by importing the pickle module: import pickle, which is needed for using the pickle function to ‘load’ the data from the file.

`vip_lst = read_data_from_file(working_file_str=default_file_str)`

The program calls the function `read_data_from_file()` where the string value (filename) assigned to the `default_file_str` variable is passed to the parameter `working_file_str`. The `vip_lst` list-variable is assigned to the output of the function.

The function `read_data_from_file()` opens the filename string value passed to the `working_file_str` parameter in read mode for binary files ( `rb` ) and assigns the file object to `file_obj` variable. The `file_obj` variable is used as an input for the `pickle` function and `.load method`. The result of the function is to output a list with dictionary data type rows which is assigned to the list_of_rows variable.

The overall structure of the `read_data_from_file` function follows this logic:
1.	Try to open the `default_file_str` as working_file_str.
2.	If file is not found, then return custom error message: “ERROR: File not found.”
3.	If file is found, then try to extract data from file to `list_of_rows` variable with `pickle.load()` function and method.
4.	`EOFError = End of file error`
5.	`Return list_of_rows` variable with data from file.

The `output_current_vip_in_list` function uses the output of the `read_data_from_file` function `list_of_rows` variable to pull each row value for `Name` and `Birthday` keys. At this point of the program, code is same as prior assignment for unpacking data from a list object with dictionary list as rows.

```
import pickle

# Data ----------------------------------------------------------- #
# Declare variables and constants

default_file_str = 'AppData.dat'

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

# Presentation (Input/Output)  ----------------------------------- #

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

# Main Body of Script  ------------------------------------------- #

# Step 1 - When the program starts, Load file.

vip_lst = read_data_from_file(working_file_str=default_file_str)

# Step 2 - Display a menu of choices to the user

while True:

# Step 3 Show current data

print('''
=====================================
DISPLAY DATA
=====================================''')

    # Step 3 Show current data
    output_current_vip_in_list(list_of_rows=vip_lst)

# Step 4 – Process user’s menu choice

if choice_str.strip() == '1':  # Add a new Task

continue

elif choice_str.strip() == '2':  # Save Data to File

continue  # to show the menu

elif choice_str.strip() == '3':  # Exit Program

break  # exit Menu loop
```

#### Menu

*Requirement 3: Allow user to select option from menu.*

To simplify coding, the program functions are reduced to Add, Save, and Exit. This code is based directly on the menu from prior assignment.

```
# Data ----------------------------------------------------------- #
# Declare variables and constants

# Processing  ---------------------------------------------------- #

# Presentation (Input/Output)  ----------------------------------- #

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

def input_menu_choice():
    choice = str(input('Select option [1 to 3]: \t\t\t| ')).strip()
    return choice

# Main Body of Script  ------------------------------------------- #

# Step 1 - When the program starts, Load file.

# Step 2 - Display a menu of choices to the user

output_menu()

choice_str = input_menu_choice()

# Step 3 Show current data

# Step 4 - Process user's menu choice
```
#### Add data

*Requirement 4: Allow user to add data.*

The program collects allows the user to input three data elements for each VIP record: Name, Relationship, and Date of birth. I defined a function for each data element to simplify the code since each element requires unique “data validation” contingencies.

The `input_vip_name` function requires the user to input a name that must be longer than 1 character. The input by the user is assigned the name variable which becomes the output value of the function: return name.

The `input_vip_circle` function captures the relationship of the VIP to the user – data which may be helpful in future version. There are 4 categories of relationship: 
1. Family, 
2. Friend, 
3. Business, and 
4. Other.

The user is required to pick one of the four. If an option is not in the range of 1 through 4 then custom error message: “ERROR: Invalid option selected. Choose number from list.” is triggered. Additionally, if the user inputs a non-numeric character (e.g., letter) then the try-except statement will trigger another custom error message: “ERROR: Non-numeric value entered. Choose number from list.” The input by the user is assigned the `circle` variable which becomes the output value of the function: return `circle`.

The `input_vip_dob` function requires the datetime module: import datetime. The try-except statement will catch occurrences where the value inputted by the user is not a valid date or if the date is not in the correct yyyy-m-d format: `datetime.datetime.strptime(dob, '%Y-%m-%d')`. If the user inputs an invalid date or incorrectly formatted date, then customer error message is triggered: “ERROR: Invalid date. Date should be in yyyy-m-d format.” The input by the user is assigned the dob variable which becomes the output value of the function: return dob.

The `row_dic` variable in the `add_data_to_list` function takes the outputs of the `input_vip_name`, `input_vip_circle`, `input_vip_dob` functions and creates a dictionary list record with and organized to the following keys, respectively: `Name`, `Circle`, `Birthday`. This `row_dic` dictionary list is appended to the `list_of_rows` list similar prior assignment. In addition to returning the `list_of_rows` list, this function also returns zero integer.

In the `vip_lst`, `check_save_flag[0] = add_data_to_list()` statement the `list_of_rows` list is assigned to the global `vip_lst` list. Additionally, zero integer is passed to the `check_save_flag` global array. If the value in the zero index of the `check_save_flag` global array is referenced later if the user chooses to quit the program without saving.

```
import datetime

# Data ----------------------------------------------------------- #
# Declare variables and constants

check_save_flag = [1]  # If = 1, then data saved/no changes, if = 0, changes \

vip_lst = []

# Processing  ---------------------------------------------------- #

# Presentation (Input/Output)  ----------------------------------- #

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
            circle = int(input('\nSpecify relationship [1-4]: \t\t|'))
            if circle in range(1, 5):
                return circle
            else:
                print('\nERROR: Invalid option selected. Choose number '
                      'from list.')
        except ValueError:
            print('\nERROR: Non-numeric value entered. Choose number from list.')

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

def output_vip_added():
    print('\n\t*********************************'
          '\n\tNew VIP added'
          '\n\t---------------------------------'
          '\n\tName: \t\t\t' + _name +
          '\n\tRelationship: \t' + c +
          '\n\tBirthday: \t\t' + _dob +
          '\n\t*********************************')

def add_data_to_list(name, circle, dob, list_of_rows):
    row_dic = {"Name": str(name).strip(),
               "Circle": str(circle).strip(),
               "Birthday": str(dob).strip()}
    list_of_rows.append(row_dic)
    return list_of_rows, 0

# Main Body of Script  ------------------------------------------- #

# Step 1 - When the program starts, Load file.

# Step 2 - Display a menu of choices to the user

while True:

# Step 3 Show current data

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
```

#### Save data

*Requirement 5: Allow user to save data.*

The program begins by importing the pickle module: `import pickle`, which is needed for using the pickle function to ‘dump’ the data from the program into the file.

When the user chooses option 2 (save data) from the menu, the program calls the `write_data_to_file` statement. If the value in the zero index of the `check_save_flag` array is zero, then the data has changed and has not been saved, so the program will proceed to save the file. If the `check_save_flag` array is one, then the `write_data_to_file` statement is not called and the program notifies the user with custom message: “ALERT: No changes detected.”

Inside the `write_data_to_file` statement, the default file specified is opened in `wb` mode because the program is writing data to a binary file. The `pickle.dump(list_of_rows, file_obj)` pickle statement, takes the `vip_lst` list of dictionaries values passed via the `list_of_rows` list array and dumps the object data into the `file_obj` which is passed via the `working_file_str` parameter. Lastly, the `check_save_flag` is changed to `1` since the data has been saved and the program notifies the user: “Data saved.”

```
import pickle

# Data ----------------------------------------------------------- #
# Declare variables and constants

default_file_str = 'AppData.dat'

check_save_flag = [1]  # If = 1, then data saved/no changes, if = 0, changes \
# not saved

vip_lst = []

# Processing  ---------------------------------------------------- #

def write_data_to_file(working_file_str, list_of_rows):
    file_obj = open(working_file_str, 'wb')
    pickle.dump(list_of_rows, file_obj)
    check_save_flag[0] = 1
    print('Data saved.')
    file_obj.close()

# Presentation (Input/Output)  ----------------------------------- #

# Main Body of Script  ------------------------------------------- #

# Step 1 - When the program starts, Load file.

# Step 2 - Display a menu of choices to the user

while True:

# Step 3 Show current data

# Step 4 - Process user's menu choice

elif choice_str == '2':  # Save Data to File
    if check_save_flag[0] == 0:
        write_data_to_file(working_file_str=default_file_str,
                           list_of_rows=vip_lst)
    else:
        print('\nALERT: No changes detected.')
    continue  # to show the menu
```

#### Quit program

*Requirement 6: Allow user to quit the program.*

*Requirement 7: Allow program to prompt user to save if unsaved changes are detected.*

When the user chooses to quit the program, the program will refer to the `check_save_flag` array value at the zero-index location. If the value is `0`, then the “Add” function had been executed by the user and the new data has not been saved. The program prompts the user with custom message: “WARNING: You have unsaved changes. If you quit, your changes will not be saved.” I got a bit lazy at this point of the program and crammed all of the logic into this block with the exception of the `output_exit_program` function for displaying the exit greeting and user-input interrupt since this code is used more than once. Similar to the prior assignment, when the user quits the program, the `break` statement is executed where the `while True` loop is exited.

```
# Data ----------------------------------------------------------- #
# Declare variables and constants

check_save_flag = [1]  # If = 1, then data saved/no changes, if = 0, changes not saved

# Processing  ---------------------------------------------------- #

# Presentation (Input/Output)  ----------------------------------- #

def output_exit_program():
    print("\n\tByeeee!")
    input("\n[Press ENTER key to quit.]")

# Main Body of Script  ------------------------------------------- #

# Step 1 - When the program starts, Load file.

# Step 2 - Display a menu of choices to the user

while True:

# Step 3 Show current data

# Step 4 - Process user's menu choice

elif choice_str == '3':  # Exit Program
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
```

### Proposed solution

The following source code is my program for Assignment07.

```
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
```

### Test

#### Procedure

For the purpose of this assignment, testing is performed in PyCharm IDE.

Open PyCharm

PyCharm > File > Open > directory path > A07-RSar.py

PyCharm > Run > “A07-RSar”

For this assignment and based on the limitations placed on the inputs of the user, I intend to limit my test cases to expected errors and a few valid input types.

##### Test Flow 1

Start program / Open data file and display contents

![Results of Test flow ID: 1](\images\test01.png "Results of Listing 13")#### Figure 1-1. Results from test: Start program

#### Results

### Execution

#### Terminal


#### Results



## Summary
Similar to preceding assignments, I thought this week’s assignment was a significant step up in complexity and challenge. Despite the program functionality being stripped down from the prior assignment, I can confirm the feeling “60% of code is exception handling”. At least, for me, it sure felt that way. Unforeseen (and highly-irregular) opportunities over this past weekend may have also effectively compressed my available time for this assignment. I think the code structures and frameworks that were provided as part of prior assignments were helpful. One challenging (and personally, frustrating) aspect of this assignment was the reliance on self-research to learn the level of coding needed to adapt prior assignments’ code. I will surely appreciate the “assignment answers” example for this module’s lessons for future reference.


## References

### Exception handling

Corey Schafter – YouTube, https://www.youtube.com/watch?v=NIWwJbo-9_8, 2022 (External site): Python Tutorial: Using Try/Except Blocks for Error Handling

  * Notes: Clear, very concise instruction, Logical progression through content

Socratica – YouTube, https://www.youtube.com/watch?v=nlCKrKGHSSk&t=10s, 2022 (External site): Exceptions in Python||Python Tutorial||Learn Python Programming
	
  * Notes: Fun, relevant, “more elaborate” example (opening .dat file)

Stack Overflow, https://stackoverflow.com/questions/2244270/get-a-try-statement-to-loop-around-until-correct-value-obtained, 2022 (External site): Get a Try statement to loop around until correct value obtained

Stack Overflow, https://stackoverflow.com/questions/2083987/how-to-retry-after-exception, 2022 (External site):  How to retry after exception?

TutorialKart, https://www.tutorialkart.com/python/python-range/python-if-in-range, 2022 (External site): Python – if in Range, if not in Range
	
  * Notes: Explicitly searched for solution to loop input_vip_data_circle()

Stack Overflow, https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python, 2022 (External site): How do I validate a date string format in python?

  * Notes: Explicitly searched for solution to validate input_vip_data_dob()

### Pickling

DelfSatck, https://www.delftstack.com/howto/python/python-read-pickle/, 2022 (External site): Read a Pickle File Using Python

  * Notes: Explicitly searched for solution on how to read all data from binary file.
