import re

string = "this is a string with random codes like 4f6@7A& and 84f6@7A&. "

pattern = r"[@&]\w{3}[@&]" # match any code that starts with @ or & and has 3 random letters in between
replace= " "

new_string = re.sub(pattern, replace, string)

print(new_string)

# output: This is a string with random codes like 4f6 and 8q2
