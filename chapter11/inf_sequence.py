def inf_squence():
    num = 0
    while True and num <= 10:
        yield num
        num += 1


for iterator in inf_squence():
    print(iterator, end=' ')
print()
