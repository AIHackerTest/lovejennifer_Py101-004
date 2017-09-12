def load_data(file):
	dic = {}
	with open(file) as f:
		try:
			document = f.readlines()
			#print(document)
			for line in document:
				info = line.split(',')
				dic[info[0]] = info[1]
		except IOError as ioerr:
			print('%s文件不存在' %(file))
		return dic

def words():
	 print('''
	      输入城市名，返回该城市的天气数据；
              输入指令，打印帮助文档（一般使用 h 或 help）；
              输入指令，退出程序的交互（一般使用 quit 或 exit）；
              在退出程序之前，会打印查询过的所有城市.
          ''')

def history(l):
	for i in range(len(l)):
		print(l[i][0], l[i][1])

def search():
	h = []
	while True:
		city = input("输入指令或城市名: ")
		d = load_data("../resource/weather_info.txt")
		if city in d.keys():
			weather = d[city]
			if [city, weather] not in h:
				h.append([city, weather])
			print('{}, {}'.format(city, weather))
		elif city in ['help','h']:
			words()
		elif city == 'history':
			history(h)
		elif city in ['exit','quit']:
			print('推出前输入历史记录: ')
			history(h)
			break
		else:
			print("请输入正确指令或城市名，输入help或h进入帮助")
			continue

if __name__ == '__main__':
	search()

