#检查特定值是否不包含在列表中
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
	print(user.title() + ",you can post a response if you wish.")

#条件测试
car = 'subaru'
print ("Is car =='subaru'?I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'?I predict False.")
print(car == 'audi')