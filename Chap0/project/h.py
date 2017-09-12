# coding=utf-8

from random import randint
from random import sample

def rand_num():
	m = [str(i) for i in range(10)]
	first_num = m.pop(randint(1, 9))
	str_other_num = "".join(map(str, sample(m, 3)))
	# str_other_num = "".join(str(x) for x in sample(m, 3))
	number = first_num + str_other_num
	return number

def get_num():
	input_num = input("Please type in a 4 digit number: ")
	if input_num.isdigit() and len(input_num) == 4:
		return input_num
	else:
		print ("Only 4 digit numbers.")
		return get_num()

def guess(wanted_num, input_num):

    count_of_a = 0
    count_of_b = 0
    
    for i, num in enumerate(wanted_num):

        if num == input_num[i]:
            count_of_a += 1
        elif num in input_num:
            count_of_b += 1
        else:
            continue

    result_bool = False
    result_str = '%dA%dB' % (count_of_a, count_of_b)

    if count_of_a == 4:
    	print ("Bravo! You win.")
    	result_bool = True
    else:
    	print (result_str)

    return (result_bool,result_str)

def play(allowable_count):

	wanted_number = rand_num()
	count = 1

	while True:

		if count > allowable_count:
			print('您没有机会猜测，游戏结束! %s' % wanted_number)
			break

		print('第%d次猜测，还有%d次机会' % (count, 10-count))
		input_number = get_num()

		if guess(wanted_number, input_number)[0] is True:
			break

		count += 1


