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



def find(sub,actual):
	
	word = ''
	count_sub = 0
	count_actual = 0
	
	for i in sub[count_sub::]:
		
		char_to_find = i		
		
		for j in actual[count_actual::]:
		
			if j != char_to_find:
				count_actual = count_actual + 1
				continue
			else:
				word = word + char_to_find
				count_actual = count_actual + 1
			break
		count_sub = count_sub + 1
		
	if word == sub:
		return True
	else:
		return False
	
#print find("is", "faisal")
#print find("fa", "faisal")
#print find("fai", "faisal")
#print find("la", "faisal")

#################################################################################

def checkPalindrome(word):

	counter_left = 0

	char_left = ''
	char_right = ''
	
	test_word = ''
	new_word = ''
	
	for char in word:
		if char != " ":
			new_word = new_word + char
	
	counter_right = len(new_word) - 1
	
	for i in new_word[counter_left::]:
		char_left = i

		for j in new_word[counter_right::-1]:
			char_right = j

			if char_right != char_left:
				return False
			else:		
				test_word = test_word + j
				counter_right -= 1
			break
			
			counter_left += 1
	
	if test_word == new_word:
		return True
	else:
		print "something went wrong"
		
#print checkPalindrome ('racecar')

#test = 'abcdef'
#for i in test[len(test)::-1]:
#	print i

###############################################################################


def sum_numbers(input_word):

	num = ''
	total = 0
	count = 0
	
	for i in range(len(input_word))[count::]:

		if input_word[i] in range(10):
			num = num + input_word[i]
			
			for j in range(len(input_word))[i+1::]:
				
				if input_word[j] in range(10):
					num = num + input_word[j]
				else:
					count = j
					break
			print num
			#total = float(total) + float(num)
	#return total				






print sum_numbers("fa21h2d")















