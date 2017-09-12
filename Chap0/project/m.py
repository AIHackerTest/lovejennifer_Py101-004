#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from random import (randint,
                    sample
                    )


def generate_randnum():

    optional_numbers = [str(i) for i in range(10)]

    first_num = optional_numbers.pop(randint(1, 9))
    
    three_num_ls = sample(optional_numbers, 3)
    three_num = ''.join(three_num_ls)

    random_num = first_num + three_num
    return random_num


def get_num():

    input_num = input('Please type in a 4 digit number.\n >')

    if input_num.isdigit() and len(input_num) == 4:
        return input_num
    else:
        print('Only a 4 digit number is wanted! e.g. 5')
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
    result_str = '{}A{}B'.format(count_of_a, count_of_b)

    if count_of_a == 4:
        print('猜对，游戏结束')
        result_bool = True

    else:
        print(result_str)
        
    return (result_bool, result_str)


def play(allowable_count):

    wanted_number = generate_randnum()

    count = 1

    while True:
    
        if count > allowable_count:
            print(f'您没有机会猜测，游戏结束!正确答案：{wanted_number}\n要不充点钱再来？')
            break
            
        print(f'第{count}次猜测，还有{10 - count}次机会')
        input_number = get_num()

        if guess(wanted_number, input_number)[0] is True:
            break
        
        count += 1

play(10)