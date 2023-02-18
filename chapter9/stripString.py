string = "      ABC        "
string.strip()
print("<" + string + ">")  # prints < ABC >, not <ABC>

anotherString = string.strip()
print("<" + anotherString + ">")  # prints <ABC>
