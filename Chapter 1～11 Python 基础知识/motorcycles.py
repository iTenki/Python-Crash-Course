motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
del motorcycles[0]
print (motorcycles)

motorcycles = ['honda','yamaha','suzuki']
del motorcycles[1]
print (motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print("The last motorcycles I owned was a " + last_owned.title() + ".")

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop(0)
print("The last motorcycles I owned was a " + last_owned.title() + ".")

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA" + too_expensive.title() + " is too expensive for me.")