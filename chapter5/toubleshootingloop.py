print("Help! my laptop doesn't work!")
done = False
while not done:
    print("dooes the computer make any sound(fans, etc)")
    choice = input("or show any lights? (y/n): ")
    # the troubleshooting control logic
    if choice == 'n':  # the computer doesn't have a power
        choice = input("Is it plugged in? (y/n): ")
        if choice == 'n':  # it is not plugged in, plug it in
            print("Plug it in. ")
        else:  # It is plugged in
            choice = input('Is the switch in the \"on\" position? (y/n): ')
            if choice == 'n':
                print("Turn it on. ")
            else:
                choice = input("Does the computer have a fuse? (y/n); ")
                if choice == 'n':
                    choice = input("Is the outlet OK? (y/n); ")
                    if choice == 'n':
                        print("Check the outlet's circuit")
                        print("breaker or fuse. move to a")
                        print("new outlet. if necessary. ")

                    else:  # beats me
                        print("Please consult a service technician. ")
                        done = True  # nothing else i can do
                else:  # check fuse
                    print("Check the fuse. Replace if ")
                    print("necessary. ")

    else:  # the computer has a power
        print("Please consult a service technician. ")
        done = True  # nothing else i can don