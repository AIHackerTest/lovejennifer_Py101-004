d = {}
history = {}
with open("../resource/weather_info.txt", "r") as stats:
	for line in stats:
		data = line.strip('\n').split(',')
		d[data[0]] = data[1]

while True:
	city = input("请输入指令或您要查询的城市名： ")
	if city in d.keys():
		history[city] = d[city]
		print(%s + '的天气状况为： ' + %s %(city, d[city]))
	elif city == 'history':
		for k, v in history.items():
			print(k, v)
		#for city in history:
		#	print(city, history[city])
	elif city in ['exit', 'quit']:
		print("显示历史记录并退出")
		for city in history:
			print(city, history[city])
		break
	elif city in ['help', 'h']:
		h = open("../resource/help.txt", "r").read()
		print(h)
	else:
		print("指令或城市不存在，请输入help查看帮助文档")
		continue

		



