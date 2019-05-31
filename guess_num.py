# 讓使用者自行設定隨機數字的範圍
# 請使用者重覆猜答案
# 如果猜對就說'你猜對了'
# 如果猜錯就提示'比答案大'或'比答案小'
# 過程中告訴使用者猜了第幾次


import random
start = input('請輸入隨機數字的開始值')
end = input('請輸入隨機數字的結束值')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count += 1
	num = input('猜一個數字: ')
	num = int(num)
	if num ==  r:
		print('你猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print ('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')

	