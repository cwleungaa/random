import random

start = input('請輸入猜數字範圍開始值: ')
end = input('請輸入猜數字範圍結束值: ')
start = int (start)
end = int (end)

r = random.randint(start,end)

i = 0

while True:

	guess = input('請猜一數字: ')

	guess = int(guess)

	if guess == r :
		print('終於猜對了')
		print('你共猜了',i+1,'次')
		break

	elif guess < r:
		print('你猜的數字比答案還少')
		i = i + 1
	else:
		print('你猜的數字比答案還大')
		i = i + 1
	print('你共猜了', i, '次')
