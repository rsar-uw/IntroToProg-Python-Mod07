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



#### Add data



#### Save data



#### Quit program



### Proposed solution



### Test

#### Procedure

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
