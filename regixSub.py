import re

pattern = '[0-9]+'
string = 'Account Number - 12345, Amount - 586.32'
repl = ' '

print("Original String")
print(string)

result = re.sub(pattern, repl, string)

print("After replacement")
print(result)


