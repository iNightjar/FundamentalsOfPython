# count to ten and print each number on its own line

def count(number: int) -> int:
    # for i in range(1, number):
    #     print(i, end=' ')
    # print("Reached to number specified") # linear search
    counter = 1
    while counter < number:
        print(counter, end=' ')
        counter += 1 
    print("Reached to specified number") # linear search


print("Going to count to ten ... ")
count(3)
