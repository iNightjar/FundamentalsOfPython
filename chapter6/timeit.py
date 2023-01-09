from time import clock

print("Your name : ", end='')
start_time = clock()
name = input()
elapsed = clock - start_time
print(name, " i took you ", elapsed, " seconds to respond. ")
