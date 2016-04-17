##test

def product(x,y,z):
	max_num = 0	
	inter_num = 0

	if x < y:
		max_num = y
		inter_num = x
		if z > y:
			max_num = z
			inter_num = y
		else:
			max_num = y
			inter_num = z
	elif x > y:
		max_num = x
		inter_num = y
		if z > x:
			max_num = z
			inter_num = x
		else:
			max_num = x
			inter_num = z
	#print max_num
	#print inter_num


#print product(5,3,4)


def prod(x):
	number = 0
	number_2 = 0

	for i in x:
		if i > number:		
			number = i			
	for j in x:
		if j == number:
			continue
		elif j > number_2:
			number_2 = j
				
	return number, number_2
		

#def Fib(n):
#	return (Fib(n-1) + Fib(n-2))
	

def reverse(sentence):
	count = 0
	new_sentence = ''
	final_sentence = ''
	counter = 0
	word = ''

	for char in sentence[::-1]:
		new_sentence = new_sentence + char


	for char in new_sentence:

		if char != " ":
			count = count + 1
			continue
		else:
			for i in new_sentence[count-1::-1]:

				if i != " ":	
					word = word + i
				else:
					break
		
		count = count + 1
		final_sentence = final_sentence + " " + word
		word = ''
	print final_sentence

reverse("I am a student")





