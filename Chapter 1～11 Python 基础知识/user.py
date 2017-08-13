#网站用户信息的字典
user_0 = {
	'username' : 'efermi',
	'first' : 'enrico',
	'last' : 'fermi',
}
for key,value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)

#favorite_languages.py
favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python',
}
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite languages is " + language.title() + ".")

#遍历字典中的键     默认遍历所有键( 可以省略key() )
for name in favorite_languages.keys():
	print(name.title())

friends = ['phil','sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print("Hi " + name.title() + " , I see your favorite languages is "
			+ favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

#遍历字典中的所有值
print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())
#set()表示集合 元素唯一性 无序性 确定性
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())
