import random

r = random.randint(1,100)

i = 1

while True:

	guess = input('請猜一數字: ')

	guess = int(guess)

	if guess == r :
		print('終於猜對了')
		print('你共猜了',i,'次')
		break

	elif guess < r:
		print('你猜的數字比答案還少')
		i = i + 1
	else:
		print('你猜的數字比答案還大')
		i = i + 1
