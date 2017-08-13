import json

def get_stored_username():
	'''如果有了用户名，就获取它'''
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	'''提示用户输入用户名'''
	username = get_stored_username()
	filename = 'usernama.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	'''问候用户，并指出其姓名'''
	username = get_stored_username()
	if username:
		print("Welcome back, " + username + "!")
	else:
		username = get_new_username()
			print("We will remember you when you come back, " + username + "!")

greet_user()
