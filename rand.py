import random

r = random.randint(1,100)

while True:

	guess = input('請猜一數字: ')

	guess = int(guess)

	if guess == r :
		print('終於猜對了')
		break

	elif guess < r:
		print('你猜的數字比答案還少')

	else:
		print('你猜的數字比答案還大')