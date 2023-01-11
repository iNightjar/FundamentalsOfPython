from time import process_time  # clock() function is now deprecated


print("Your name : ", end='')
start_time = process_time()
name = input()
elapsed = process_time() - start_time
print(name, " i took you ", elapsed, " seconds to respond. ")
