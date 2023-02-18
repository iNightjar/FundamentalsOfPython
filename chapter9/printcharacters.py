string = "ABCDEFGHIJK"
print(string)
for iterator in range(len(string)):
    print("[", string[iterator], "]", sep="", end="")

print()  # print newline

for character in string:
    print("<", character, ">", sep="", end="")
print()  # print newline
