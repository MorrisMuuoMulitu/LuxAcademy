import random
import string

#create a function that generates a random password
def my_password(length,num=False,strength='weak'):
	"""length of password if you want a number, and the strength as (weak,strong,very_strong)"""
	lower=string.ascii_lowercase
	upper=string.ascii_uppercase
	letter=lower+upper
	digits=string.digits
	punctuation=string.punctuation
	pwd=''
	if strength=='weak':
		if num:
			length-=2
			for i in range(2):
				pwd+=random.choice(digits)
		for i in range(length):
			pwd+=random.choice(lower)

	elif strength=='strong':
		if num:
			#increase the length of the password by 2
			length-=2
			for i in range(2):
				pwd+=random.choice(digits)
		for i in range(length):
			pwd+=random.choice(letter)
	elif strength=='very_strong':
		ran=random.randint(2,4)
		if num:
			length-=ran
			for i in range(ran):
				pwd+=random.choice(digits)
		length-=ran
		for i in range(ran):
			pwd+=random.choice(punctuation)
		for i in range(length):
			pwd+=random.choice(letter)
	#Make is a list for shuffling
	pwd=list(pwd)
	random.shuffle(pwd)
	return ''.join(pwd)

print ("Weak Password:",my_password(8,num=False,strength='weak'))
print("Strong Password:",my_password(8,num=False,strength='strong'))
print("Very Strong Password:",my_password(8,num=True,strength='very_strong'))

	
