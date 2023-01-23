# count to ten and print each number on its own line

def count(number: int) -> int:
    for i in range(1, 11):
        print(i + number, end=' ')
    print()


print("Going to count to ten ... ")
count(2)
