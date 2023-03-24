import pprint

contacts = {}  # the global telephone contact list
running = True

while running:
    command = input('A)add , D)elete , L)ook up , Q)uit: ')
    if command == 'A' or command == 'a':
        name = input("Enter name: ")
        print('Enter number for ', name, end=': ')
        number = input()
        contacts[name] = number
    elif command == 'D' or command == 'd':
        del contacts[name]
    elif command == 'L' or command == 'l':
        name = input("Enter name to look for: ")
        print(f"*** Found {name} >> ", contacts[name])
    elif command == 'Q' or command == 'q':
        running = False
    elif command == 'dump':
        pprint.pprint(contacts)
    else:
        print("Invalid Input. ")
