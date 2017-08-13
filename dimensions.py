#元组
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#遍历元组中的所有值
dimensions = (200,50)
for dimension in dimensions:
	print(dimension)

#修改元组变量
dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimension = (400,100)
print("\nModified dimensions")
for dimenson in dimensions:
	print(dimenson)
