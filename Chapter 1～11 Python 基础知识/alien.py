#简单的字典  使用字典  访问字典中的值
alien_0 = {'color': 'green', 'points': 5 }
print(alien_0['color'])
print(alien_0['points'])

new_point = alien_0['points']
print("You just earned " + str(new_point) + " points!")

#字典添加键-值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#字典不关心键-值的顺序，只关心键-值的关系。

#分行对字典添加键-值
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#修改字典键-值
alien_0 = {'color' : 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is " + alien_0['color'] + ".")

alien_0 = {'x_position' : 0,'y_position' : 25,'speed' : 'meidum' }
print("Original x_position: " + str(alien_0['x_position']))
#向右移动外星人
#据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] =='meidum':
	x_increment = 2
else:
	#这个外星人的速度一定很快
	x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: " + str(alien_0['x_position']))

#删除字典键-值
alien_0 = {'color': 'green' , 'points' : 5}
print(alien_0)
del alien_0['points']
print(alien_0)

#由类似对象组成的字典
favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python'
}
print("Sarah's favorite languages is " +
	favorite_languages['sarah'].title() +
	".")

