file_name = 'Alice in Wonderland.txt'

try:
	with open(file_name) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + file_name + " does not exist."
	print(msg)
else:
	# 计算文件大致包含多少单词
	words = contents.split()
	numb_words = len(words)
	print("The file " + file_name +  " has about " + str(numb_words) + " words.")                   