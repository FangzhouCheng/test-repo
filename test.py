print "Hello Fangzhou"

#inp = raw_input("European floor?")
#usf = int(inp) +1
#print "US floor", usf

def greet(lang):
	if lang == "es":
		print "Hola"
	else: print "Hello"
greet("es")
greet(123)
greet("en")

a = "hello"
b = a + " " + "world"
print b

b = "fruit"
for letter in b:
	print letter
	
lst = list()
words = [1,2,3]
for w in words:
	if w in lst: continue
	lst.append(w)
print lst

stuff = "0.312"
y = stuff[1]
print y

num = raw_input("position:")
num = int(num)
list = range(num)
x = 3
x = list[2]
print x

#0,1,2,3,4
#1,2,3,5,8,13,21,34


