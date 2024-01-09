# This is an alternative version of the scribe_test.py file
# I have tried to use functions to simplify the code and make it more readable
# However, using functions means that any formatting changes can't be saved"
# for example, i enter a simple string Hello World
# if I bold Hello, then try to underline World, the program returns World in underline, but Hello is not in bold
# the issue is likely that variables in a function cannot be used outside that function
# I would be grateful for any feedback on how to resolve this issue / improve the code 


MAIN_MENU = "Would you like to:\n1. Edit the text\n2. Format the text\n3. View the current version of the text\n4. Exit\n"
FORMAT_MENU = "Please select the format you would like to apply:\n1. Bold\n2. Italics\n3. Underline\n4. Change case\n5. Undo change\n"

string = input("Please enter your text: ")

print(f"Thank you. You have entered: {string}.")

def bold(list, string):
    for i in list:
        new_string = string.replace(i,"\033[1m"+i+"\033[0m")
        string = new_string
    print("You have selected Bold. The amended text is: "+string)
    return string

def italics(list, string):
    for i in list:
        new_string = string.replace(i,"\033[3m"+i+"\033[0m")
        string = new_string
    print("You have selected Italics. The amended text is: "+string)
    return string

def underline(list, string):
    for i in list:
        new_string = string.replace(i,"\033[4m"+i+"\033[0m")
        string = new_string
    print("You have selected Underline. The amended text is: "+string)
    return string

def upper_case(list, string):
    for i in list:
        new_string= string.replace(i,i.upper())
        string = new_string
    print("You have selected UPPER CASE. The amended text is: "+string)
    return string

def lower_case(list, string):
    for i in list:
        new_string= string.replace(i,i.lower())
        string = new_string
    print("You have selected LOWER CASE. The amended text is: "+string)
    return string

def undo(list, string):
    for i in list:
        new_string = string.replace(i,"\033[0m"+i+"\033[0m")
        string = new_string
    print("You have selected Undo. The amended text is: "+string)
    return string

done = False

while not done:

    choice = input(MAIN_MENU)

    while choice not in ["1","2","3","4"]:
        print("That is not a valid entry. Please select an option from the menu below")
        choice = input(MAIN_MENU)

    if choice == "1":
        print("You have selected Edit text")
        selection = input("Please enter the text you would like to change: ")
        select_list = selection.split()
        error_count = 0
        for i in select_list:
            if i not in string:
                error_count += 1
        while error_count > 0:    
            print("That is an invalid entry. Your selection does not appear in the text")
            selection = input("Please enter the text you would like to change: ")
            select_list = selection.split()
            error_count = 0
            for i in select_list:
                if i not in string:
                    error_count += 1
        replace = input("Please enter the new text: ")
        replace_list = replace.split()
        for i in range(len(select_list)):
            new_string = string.replace(select_list[i],replace_list[i])
            string = new_string
        print("The amended text is: "+string)

    elif choice == "2":
        selection = input("Please enter the text you would like to format: ")
        select_list = selection.split()
        error_count = 0
        for i in select_list:
            if i not in string:
                error_count += 1
        while error_count > 0:    
            print("That is an invalid entry. Your selection does not appear in the text")
            selection = input("Please enter the text you would like to format: ")
            select_list = selection.split()
            error_count = 0
            for i in select_list:
                if i not in string:
                    error_count += 1
        print("Thank you. You have selected: "+selection)
        style = input(FORMAT_MENU)
        while style not in ["1","2","3","4","5"]:
            print("That is not a valid entry. Please select an option from the menu below")
            style = input(FORMAT_MENU)
        if style == "1":
            bold(select_list, string)
            string = string
        elif style == "2":
            italics(select_list, string)
            string = string
        elif style == "3":
            underline(select_list, string)
            string = string
        elif style == "4":
            case = input("Would you like to change to 1. UPPER CASE or 2. lower case?")
            if case == "1":
                upper_case(select_list, string)
                string = string
            if case == "2":
                lower_case(select_list, string)
                string = string
        elif style == "5":
            undo(select_list, string)
            string = string              
    
    elif choice == "3":
        print("The current version of the text is: "+string)
    
    elif choice == "4":
        done = True
        print("Thank you for using Simple Scribe")


