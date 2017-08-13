#简单的IF语句
age = 19
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")

#if-else语句
age = 17
if age >=18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else :
	print("Sorry you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")

#if-elif-else
age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else :
	print("Your admission cost is $10.")

if age < 4:
	price = 0
elif age < 18:
	price = 5
else :
	price = 10
print("Your admission cost is $" + str(price) + ".")

#多个elif代码块
age = 12
if age < 4 :
	price = 0
elif age < 18 :
	price = 5
elif age <65 :
	price = 10
else:
	price = 5
print("Your admission cost is $" + str(price) + ".")

#省略else代码块
age = 12
if age < 4 :
	price = 0
elif age < 18 :
	price = 5
elif age <65 :
	price = 10
elif age >=65 :
	price = 5
print("Your admission cost is $" + str(price) + ".")

#确定列表不是空的
requested_toppings = []
if requested_toppings:  #列表中有值为True，否则为False
	for requested_topping in requested_toppings :
		print("Adding " + requested_topping + '.')
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

#多个列表
available_toppings = ('mushroom','olives','green peppers','pepperoni','pineapple','extra cheese')
requested_toppings = ['mushroom','french fries','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza")
