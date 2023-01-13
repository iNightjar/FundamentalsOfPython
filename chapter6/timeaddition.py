from time import process_time

sum = 0  # initialze sum accumelator

start = process_time()
print(start)
for n in range(1, 1000000001):
    sum += n
print(sum)
elapsed = process_time() - start  # stop the stopwatch
print("sum: ", sum, "& time:",  elapsed)
