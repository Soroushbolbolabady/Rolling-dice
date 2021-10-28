import random




def random_number(n):
	number = random.randrange(1 , n)
	return number



while True :

	roll_side = int(input("How many side dice had?? : "))
	if roll_side > 1:
		print("Random number is :" + str(random_number(roll_side)))
	else : 
		print("You must enter a number bigger than 1!!!")

	another_one = int(input("Do you want do it again?!(1.yes 2.no) :"))

	if another_one == 1 :
		 True

	elif another_one == 2 :
		exit()
	else :
		print("You enter Incorrect number !!")
		exit()
