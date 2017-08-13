cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse = True)
print(cars)

cars = ['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
print(sorted(cars,reverse = True))

cars = ['bmw','audi','toyota','subaru']
print()
cars.reverse()
print(cars)

cars = ['bmw','audi','toyota','subaru']
len(cars)

#if语句 条件测试
cars = ['audi','bmw','subaru','toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

#检查值是否相等
car = 'bmw'
car == 'bmw'

car = 'Audi'
car.lower() = 'audi'