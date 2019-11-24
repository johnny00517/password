password = 'a123456'

y = 3
while y > 0:
	x = input('請輸入密碼: ')
	if x == password:
		print('登入成功')
		break

	else:
		y = y - 1
		print('密碼錯誤還有', y, '次機會')	
			
