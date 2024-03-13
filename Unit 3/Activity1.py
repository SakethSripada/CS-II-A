states =[]

def menu():
    print("Insert/Append a state, (Type 'append' or 'a')")
    print("Remove a State (Type 'remove' or 'r')")
    print("Search for a State (Type 'search' or 's')")
    print("Modify an Existing State (Type 'modify' or 'm')")
    print("Print the List (Type 'print' or 'p')")
    print("Quit (Type 'quit' or 'q')")

def validate(prompt, options):
    while True:
        user_input = input(prompt).lower()
        if user_input in options:
            return user_input
        else:
            print("Sorry. That input is not valid")

while True:
    user_choice = validate("Choose an option: ", ['append', 'a', 'remove', 'r', 'search', 's', 'modify', 'm', 'print', 'p', 'quit', 'q'])
    if user_choice in ["append", "a"]:
        state = input("Enter the state name you want to add")
        pos = input("Enter the index of where you want to enter it, if you dont wish to do so, press Enter.")
        if pos:
            index = int(pos)
            states.insert(index-1, state)
            print(f"{state} was added to the list at position {index}")
        else:
            states.append(state)
            print(f"{state} was added to the list")
            menu()
    elif user_choice in ["remove", "r"]:
        state = input("Type the name of the state you wish to remove")
        if state in states:
            states.remove(state)
            print(f"{state} was removed")
            menu()
    elif user_choice in ["search", "s"]:
        state = input("Type the name of the state you wish to search for")
        if state in states:
            pos = states.index(state)
            print(f"{state} was found in the list at position {pos+1}")
            menu()
    elif user_choice in ["modify", "m"]:
        state_to_replace = input("Which state do you wish to replace?")
        if state_to_replace in states:
            state = input("Which state do you want in its place")
            pos = states.index(state_to_replace)
            states[pos] = state
            print(f"{state_to_replace} replaced by {state}.")
        else:
            print("That state does not exist")
            menu()
    elif user_choice in ["print", "p"]:
        for state in states:
            print(state)
    elif user_choice in ["quit", "q"]:
        states.sort()
        for state in states:
            print(state)
        break