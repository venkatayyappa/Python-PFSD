import re
str1 = "i'm Lucky Ayyappa"
matches1 = re.findall("a",str1)
print(matches1)
matches2 = re.findall("i'm",str1)
print(matches2)
matches3 = re.findall("Luc",str1)
print(matches3)
matches4 = re.findall("Ayyappa",str1)
print(matches4)