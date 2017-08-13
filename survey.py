class AnonymousSurvey():
	"""收集匿名调查问卷的答案"""
	def __init__(self, question):
		"""存储一个问题，并为储存问题答案做准备"""
		self.question = question
		self.responses = []

	def show_question(self):
		"""显示调查问卷"""
		print(question)

	def store_response(self, new_response):
		self.responses.append(new_response)

	def show_results(self):
		"""显示收集到的所有答案"""
		print("Survey results:")
		for response in responses:
			print("- " + response)