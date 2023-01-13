from time import process_time

max_value = 1000
count = 0
start_time = process_time()  # start timer

# try values from 2 (smallest prime number) to max_value

for value in range(2, max_value + 1):
    is_prime = True
    for trail_factor in range(2, value):
        if value % trail_factor == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
print()
elapsed = process_time() - start_time  # Stop the timer
print("Count: ", count, " Elapsed time: ", elapsed, "sec")
