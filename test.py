#!/usr/bin/python3
#probando 2do commit en github

print("Test")

animals = open("text.txt", "r+")
text = animals.read()
#print(text)
animals.seek(0)
for animal in animals:
    print(animal)

animals.write("tigre\n")
animals.write("puma\n")

animals.close()


#lista y dicc
"""dicc = {}
dicc["nombre"]="Cris"
dicc["ciudad"]="capital"
dicc["edad"]=41
print (dicc["nombre"], dicc["edad"])
dicc["nombre"]="Cristian"

for k, v in dicc.items():
    print(k,"=>", v)"""


#while
"""age=18
while age < 30:
    print ("no tan grande",age)
    age += 1"""

#select 
"""name="test 1234"
first=name[0:7]
print(first)"""
#test
"""frase=input("Ingrese: ")
a=frase
print(a)"""
