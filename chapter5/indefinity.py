done = False
entry = int(input("Please enter number. "))
while not done:
    if entry == 100:
        print("Limit reached. ", entry)
        done = True
    else:
        print(entry)
        entry +=1

print("done")