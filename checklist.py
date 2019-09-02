
checklist = list()

# CREATE
def create(item):
    # Create item code here
    checklist.append(item)

# READ
def read(index):
    # Read code here
    print(checklist[index])

# UPDATE
def update(index, item):
    # Update code here
    checklist[index] = item

# DESTROY
def destroy(index):
    # Destroy code here
    checklist.pop(index)

def error_message():
    print("Uh-oh, looks like theres no item there!")

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    #Add code here that marks an item as completed
    i = 0
    while(i < len(checklist)):
        if(i == index):
            #print("√ {}".format(checklist[i]))
            checklist[i] = checklist[i] + " √"
        i += 1
    list_all_items()

def mark_uncompleted(index):
    #Add code here that marks an item as completed
    i = 0
    while(i < len(checklist)):
        if(i == index):
            #print("√ {}".format(checklist[i]))
            checklist[i] = checklist[i].replace(" √", "")
        i += 1
    list_all_items()

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def select(function_code):
    # Create item
    if function_code == "C" or function_code == "c":
        input_item = user_input("Input item:\n")
        create(input_item)
        return True

    # Read item
    elif function_code == "R" or function_code == "r":
        item_index = int(user_input("Index Number?\n"))
        # Remember that item_index must actually exist or our program will crash.
        if (item_index >= len(checklist)):
            error_message();
        else:
            read(item_index)

        return True

    # Print all items
    elif function_code == "P" or function_code == "p":
        if(len(checklist) < 1):
            print("Looks like the list is empty!")
        else:
            list_all_items()
        return True

    #mark item as completed
    elif function_code == "M" or function_code == "m":
        list_all_items()
        mark_completed(int(user_input("Mark which item is completed(by index):\n")))
        return True

    elif function_code == "X" or function_code == "x":
        list_all_items()
        mark_uncompleted(int(user_input("Mark which item do you want to uncheck?(by index):\n")))
        return True

    elif function_code == "U" or function_code == "u":
        list_all_items()
        to_change = int(user_input("Which item would you like to change?(by index):\n"))
        if to_change >= len(checklist):
            error_message();
        else:
            change_to = user_input("What would like to change it to?:\n")
            update(to_change, change_to);

        return True

    elif function_code == "D" or function_code == "d":
        if(0 >= len(checklist)):
            print("Looks like the list is empty!")
            return True
        else:
            list_all_items()
            deleteIndex = int(user_input("Which item would you like to delete?(by index):\n"))
            if(deleteIndex >= len(checklist)):
                error_message();
            else:
                destroy(deleteIndex)
            return True

    elif function_code == "Q" or function_code == "q":
        # This is where we want to stop our loop
        return False

    elif function_code == "T" or function_code == "t":
        # This is where we want to stop our loop
        # found at https://stackoverflow.com/questions/2084508/clear-terminal-in-python
        print(chr(27) + "[2J")
        return True
    # Catch all
    else:
        print("Unknown Option\n")
        return True

def test():
    # Add your testing code here
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    #print(read(1))

    list_all_items()

    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run

    user_value = user_input("Please Enter a value:")
    print(user_value)

#color help found at https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[91m'
    WARNING = '\033[88m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#test()
# QUESTION:
running = True
while running:
    print(bcolors.UNDERLINE + "Warning: No active frommets remain. Continue?"
      + bcolors.ENDC)
    running = select(user_input("Press\n \
    C to add to list,\n \
    R to Read from list,\n \
    P to display list,\n \
    U to update an item,\n \
    M to mark an item as completed,\n \
    X to unmark an item as completed,\n \
    D to take an item out of the checklist,\n \
    T to clear the terminal,\n \
    and Q to quit\n"))
