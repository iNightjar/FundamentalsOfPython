print("Help! My computer doesn't work!")
print("Does the computer make any sounds (fans, etc.)")
choice = input("Or show any lights? (y/n)")
# the roubleshooting control logic
if choice == 'n':  # the computer does not have power
    choice = input("Is it plugged in? (y/n)")
    if choice == 'n':  # it is not plugged in, plug it in
        print("Plug it in. If the problem persists, ")
        print("please run this program again.")
    else:  # it is pluged in
        choice = input("Is the switch in the \"on\" position? (y/n): ")
        if choice == 'n':  # the switch is off, turn it on!
            print("Turn it on. If the problem persists, ")
            print("Please run this program again. ")
        else:  # the switch is on
            choice = input("Does the computer have a fuse? (y/n): ")
            if choice == 'n':  # No Fuse
                choice = input("Is the outlet Ok? (y/n):")
                if choice == 'n' : # fix outlet
                    print("Check the outlet's circuit")
                    print("breaker or fuse. Move to a")
                    print("new outlet, if necessary. ")
                    print("If the problem persists, ")
                    print("please run this program again.")
                else: # Beats me
                    print("Please consult a service technician. ")
            else: # check fuse
                print("Check the fuse. Replace if ")
                print("necessary. If the problem")
                print("persists, then")
                print("please run this program again. ")
else: # the computer has power
    print("Please consult a service technician. ")
