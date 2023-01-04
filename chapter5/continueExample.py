sum = 0
done = False

while not done:
    val = int(input("Enter positive integer (!! 999 Quits  !!): "))
    if val < 0:
        print("Negative value", val, "ignored")
        continue  # skip the rest of body for this iteration
    if val != 999:
        print("Tallying", val)
        sum += val
    else:
        # 999 entry exists loop, if equals to 999 >> done = True
        done = (val == 999)

print("sum =", sum)
