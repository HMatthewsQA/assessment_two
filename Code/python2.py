	# INSTRUCTIONS

	# In case it is not clear, the Question appears first, then examples, then any hints and finally the function that you need to complete appears underneath:

	# <QUESTION>

	# <EXAMPLES>

	# <HINT>

	# You are NOT allowed access to the internet for this assessment, instead you should use the DOCUMENTATION that comes bundled with your Python installation.  You should already be comfortable accessing this documentation, but to summarise:

	# Access Python from you CLI

	# Type help() or for example help(str)



	# <QUESTION 1>    
	
	# Given a string, return a string where for every char in the original string, there are three chars.
	
	# <EXAMPLES>

	# one("The") → "TTThhheee"
	# one("AAbb") → "AAAAAAbbbbbb"
	# one("Hi-There") → "HHHiii---TTThhheeerrreee"

	# <HINT>
	# How does a for loop iterate through a string?

def one(input):
	newstring = ''
	for x in input:
		newstring = newstring + x
		newstring = newstring + x
		newstring = newstring + x
	return newstring

	# <QUESTION 2>

	#  Write a function which returns the boolean True if the input is only divisible by one and itself.
	
	# The function should return the boolean False if not.

	# <EXAMPLES>

	# two(3) → True
	# two(8) → False

	# <HINT>
	# What operator will give you the remainder?
	# Use your CLI to access the Python documentation and get help manipulating strings - help(range).

def two(num):
	isprime = False
	if num > 1:
		if num == 2:
			isprime = True
		for i in range(2,num):
			if (num % i) == 0:
				isprime = False
				break
			else:
				isprime = True
	else:
		isprime = False
	return isprime

	# <QUESTION 3>

	# Write a function which takes an integer input, a, and returns the sum a+aa+aaa+aaaa.

	# So if 2 was the input, the function should return 2+22+222+2222 which is 2468.

	# <EXAMPLES>

	# three(9) → 11106
	# three(5) → 6170

	# <HINT>
	# What happens if you multiply a string by a number?

def three(stringint):
	mylist = []
	mysum = 0
	stringint = str(stringint)
	mylist.append(stringint)
	mylist.append(stringint*2)
	mylist.append(stringint*3)
	mylist.append(stringint*4)
	mysum = int(mylist[0]) + int(mylist[1]) + int(mylist[2]) + int(mylist[3])
	return mysum

	# <QUESTION 4>

	# Given two Strings of equal length, 'merge' them into one String.

	# Do this by 'zipping' the Strings together.

	# Start with the first char of the first String.
	# Then add the first char from the second String.
	# Then add the second char from the first String.
	# And so on.

	# Maintain case.

	# You will not encounter whitespace.
	
	# <EXAMPLES>

	# four("String","Fridge") → "SFtrriidngge"
	# four("Dog","Cat") → "DCoagt"
	# four("True","Tree") → "TTrrueee" 
	# four("return","letter") → "rleettutrenr"

	# <HINT>
	# Use your CLI to access the Python documentation and get help manipulating strings - help(list.insert).
	# How would you seperate a string into characters?

def four(stringone, stringtwo):
	mylist = []
	counter = 0
	newstring = ""
	for i in range(len(stringone)):
		mylist.insert(counter,stringone[i])
		counter += 1
		mylist.insert(counter,stringtwo[i])
		counter += 1
	for x in mylist:
		newstring = newstring + x
	return newstring

	# <QUESTION 5>

	# Write a function to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
	
	# <EXAMPLES>
	
	# five() → [100,102,122,198,200]
	# five() → [108,104,106,188,200]
	# five() → [154,102,132,178,164]
	
	# <HINT>
	# There is a module which can be used to generate random numbers, this module is called random.
	# The random module contains a function called randint.

def five():
	import random
	intlist = []
	myint = 0
	while len(intlist) < 5:
		myint = random.randint(100, 200)
		if myint % 2 == 0:
			intlist.append(myint)
	return intlist

	# <QUESTION 6>

	# Given a string, return the boolean True if it ends in "py", and False if not. 
	
	# Ignore Case.

	# For Example:

	# six("ilovepy") → True
	# six("welovepy") → True
	# six("welovepyforreal") → False
	# six("pyiscool") → False

	# <HINT>
	# There are no hints for this question.
	
def six(input):
	checkstring = input.lower()
	check = checkstring.endswith('py')
	return check

	# <QUESTION 7>

	# Given three ints, a b c, one of them is small, one is medium and one is large. 
	
	# Return the boolean True if the three values are evenly spaced, so the
	# difference between small and medium is the same as the difference between
	# medium and large. 
	
	# Do not assume the ints will come to you in a reasonable order.
	
	# <EXAMPLES>

	# seven(2, 4, 6) → True
	# seven(4, 6, 2) → True
	# seven(4, 6, 3) → False
	# seven(4, 60, 9) → False

	# <HINT>
	# There is a function for lists called sort.
	# Use the cli to access the documentation help(list.sort)

def seven(a, b, c):
	intlist = []
	intlist.append(a)
	intlist.append(b)
	intlist.append(c)
	intlist.sort()
	difa = intlist[2] - intlist[1]
	difb = intlist[1] - intlist[0]
	if difa == difb:
		return True
	else:
		return False

	# <QUESTION 8>

	# Given a string and an integer, n, return a string that removes n letters from the 'middle' of the string.
	
	# The string length will be at least n, and be odd when the length of the input is odd, so there will always be a 'middle'.

	# <EXAMPLES>

	# eight("Hello", 3) → "Ho"
	# eight("Chocolate", 3) → "Choate"
	# eight("Chocolate", 1) → "Choclate"

	# <HINT>
	# Use the cli to access the documentation help(str.replace)

def eight(input,  a):
	replaced = ''
	length = int((len(input) - a)/2)
	length2 = int(length + a)
	start = input[0:length]
	end = input[length2:]
	output = start + end
	return output

	# <QUESTION 9>
	# Given two string inputs, if one can be made from the other return the boolean True, if not return the boolean False.

	# <EXAMPLES>

	# nine("god", "dog") → True
	# nine("tree", "tiredest") → True
	# nine("cat", "dog") → False
	# nine("tripping", "gin") → True

	# <HINT> 
	# There are no hints for this question.

def nine(string1, string2):
	check = False
	counter = 0
	for x in string1:
		for y in string2:
			if x == y:
				counter +=1
				if counter == len(string1):
					check = True
					break
	counter = 0
	for a in string2:
		for b in string1:
			if a == b:
				counter +=1
				if counter == len(string2):
					check = True
					break


	return check

	# <QUESTION 10>

	# Write a function which takes 2 integers greater than 0, X,Y as input and generates a 2-dimensional array. 
	
	# The element value in the i-th row and j-th column of the array should be i*j.

	# <EXAMPLES>

	# ten(3,2) → [[0,0,0],[0,1,2]]
	# ten(2,1) → [[0,0]]
	# ten(3,4) → [[0,0,0],[0,1,2],[0,2,4],[0,3,6]]

	# <HINT>
	# Think about nesting for loops.

def ten(X,Y):
	arraylist = []
	inputlist = []
	countX = 0
	countY = 0
	while countY < Y:
		while countX < X:
			inputlist.append(countX*countY)
			countX += 1		
		arraylist.append(inputlist)
		inputlist = []
		countY += 1
		countX = 0
	return arraylist