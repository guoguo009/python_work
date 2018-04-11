import matplotlib.pyplot as plt

class test(object):
	num = []
	def __init__(self, _list):
		super(test, self).__init__()
		self.num = _list

	def prt(self):
		print(self.num)

	def tplt(self):
		plt.plot(self.num)
		plt.show()
