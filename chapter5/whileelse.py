# add five nonnegative numbers supplied by the user
count = sum = 0
print("Please provide five nonnegative numbers when prompted. ")
while count < 5:
    # Get value from the user
    entry = float(input("Enter numbers: "))
    if entry < 0 :
        print("negative numbers not acceptable! Terminating")
        break
    sum += entry
    count+=1 
else:
    print('avarage is:', sum/count)