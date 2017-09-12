# coding=utf-8

from random import randint
import h

def guess_number():
	answer = randint(0, 20)
	times = 10
	while times > 0:
		guess = input ("请输入数字：")
		if guess.isdigit():
			if int(guess) > answer:
				print ("比正确答案大了")
				times = times - 1
				if times == 0:
					print ("结束")
				else:
					print ("你还有 %d 次机会可以输入" % times)
			elif int(guess) < answer:
				print ("比正确答案小了")
				times = times - 1
				if times == 0:
					print ("结束")
				else:
					print ("你还有 %d 次机会可以输入" % times)
			else:
				print ("答案正确，答案就是 " + str(answer))
				print ("结束")
				break
		else:
			print ("请确保你输入的是数字")
			

def main():
	while True:
		print ("请输入玩家的名字, 输入CTRL+C退出游戏:")
		input ()
		level = input ("输入你想玩的游戏级别，1 或 2, 输入0退出游戏: ")
		if level == "1":
			guess_number()
		elif level == "2":
			h.play(10)
		elif level == "0":
			break
		else:
			print ("不按要求玩，拜拜！")

main()


