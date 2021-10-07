# def rem_char_string(s,c):

# 	new_string = s.replace(c,"")
# 	return new_string


# res = rem_char_string("sravanthi", "a")

# print(res)



string1 = "sravanthi bagani"

print(string1.find("s")) # prints index of first occurence of the char

print(string1.rfind("a")) # prints last occurence index of the char

print(string1.count("a")) # prints number of times the char is repeating

print(string1.split(" "))

print(string1.replace("a","$"))

print(string1.index("b"))


list1 = [1,2,3,4,5]

print(list1.append(6))

print(list1.copy())

print(list1.count(4))

print(list1.index(5))

print(list1.pop())

print(list1.remove(1))
print(list1)

list1.insert(0,1)
print(list1)

list1.reverse()
print(list1)



dict1 = {
	"brand" : "ford",
	"model" : "Mustang",
	"year" :1964,
	"color":["red","yellow","blue"]
}

print(dict1["year"])

print(len(dict1))

print(dict1["color"][0])

print(dict1.keys())

print(dict1.items())

# dict1.update({"year":2020})

for x, y in dict1.items():
	print(x,y)



























