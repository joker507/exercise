#用于求大学物理实验中的A类不确定度和平均值，今后将考虑自动取好不确定度的有效数字和求解b类不确定度并取相应的有效数字并计算总不确定度，但现实践有限，不做实现
#physics average,求平均值
def phsaver(a):
	m = len(a)
	aver = []
	for i in range(m):
		sum = 0
		for num in a[i]:
			sum = sum + num
		aver.append(sum/len(a[i]))
	return aver
#physics undecided 求A类不确定度
def phsunde(a):
	m = len(a)
	ud = []
	for i in range(m):
		ud.append(0)
	for j in range(m):
		ave = phsaver(a)[j]
		sum = 0
		dim = len(a[j])
		for num in a[j]:
			sum = sum + (num - ave)**2
		unde = (sum/(dim*(dim - 1)))**0.5
		print ("第",j+1,"行的平均值为：",ave)
		print ("第",j+1,"行的A类不确定度为：",unde)
	return ud
if __name__ == "__main__":

	try:

		while 1:
			a = input('请输入要计算的表格，同行用,(英文逗号）分隔，换行用;(英文分号）分隔：\n')
			a = a.split(";")
			s = len(a)
			for i in range(s):
				a[i] = a[i].split(',')
				n = len(a[i])
				for j in range(n):
					a[i][j] = eval(a[i][j])
			phsunde(a)
			key = input("是否继续计算(y/n)")
			if key == 'n':
				break
	except:
		print("输入错误")


