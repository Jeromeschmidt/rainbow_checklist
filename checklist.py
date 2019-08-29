checklist = list()

# CREATE
def create(item):
    # Create item code here
    checklist.append(item)

# READ
def read(index):
    # Read code here
    return checklist[index]

# UPDATE
def update(index, item):
    # Update code here
    checklist[index] = item

# DESTROY
def destroy(index):
    # Destroy code here
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

#def mark_completed(index):
    # Add code here that marks an item as completed

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = raw_input(prompt)
    return user_input

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = int(user_input("Index Number?"))

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        # This is where we want to stop our loop
        return False

    # Catch all
    else:
        print("Unknown Option")
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

test()

running = True
while running:
    selection = user_input("Press C to add to list, R to Read from list, P to display list, and Q to quit\n")
    running = select(selection)
