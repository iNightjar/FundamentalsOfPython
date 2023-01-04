sum = 0
done = False

while not done:
    val = int(input("Enter positive integer (!! 999 Quits  !!): "))
    if val < 0 or type(val) == str:
        print("Value: ", val, "ignored.")
    else:
        if val != 999:
            print("Tallying", val)
            sum += val
        else:
            done = (val == 999)  # if True , exits the loop
print("Total Sum:", sum)
