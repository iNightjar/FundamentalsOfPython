f = open('data.txt')  # default mode is R > read
for line in f:
    print(line.strip())
f.close()


# 'r' opens the file for reading
# 'w' opens the file for writing; creates a new file
# 'a' opens the file to append data to it
