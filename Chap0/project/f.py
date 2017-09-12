"""
升级版猜数字小游戏，实现以下功能：
程序内部用 0-9 生成一个 4 位数，每个数位上的数字不重复，且首位数字不为零，如 1942
用户输入 4 位数进行猜测，程序返回相应提示
用 A 表示数字和位置都正确，用 B 表示数字正确但位置错误
用户猜测后，程序返回 A 和 B 的数量
比如：2A1B 表示用户所猜数字，有 2 个数字，数字、位置都正确，有 1 个数字，数字正确但位置错误
猜对或用完 10 次机会，游戏结束
 """

from random import randint

def generate_num():
    while True:
        num = randint(1000,9999)
        numlist = [int(i) for i in str(num)]
        if (len(set(numlist)) )==4:
            break
    return num

def verify_number(n1,n2):
    if (n1 == n2):
        return len(str(n1)),0
    else:
        numlist1 = [int(i) for i in str(n1)]
        numlist2 = [int(i) for i in str(n2)]
        numlist = [x - y for x,y in zip(numlist1,numlist2)]
        counta = numlist.count(0)
        return counta,len(set(numlist1) & set(numlist2)) - counta

        #2058
        #7010

# generate a random number
rand = generate_num()
print("Welcome to Bulls and Cows, you have 10 trials to guess right the system random number, enjoy!")
count = 1
while count <= 10:
    try:
        number = int(input(f"{count}:Please enter a 4-digit number between 1000 and 9999:"))
    except:
        print ("Please make sure you enter a number between 1000 and 9999! ")
        continue
    else:
        if number < 1000 or number >= 10000:
            print ("Number out of range, please make sure you enter a value between 1000 and 9999")
            continue
        counta,countb = verify_number(number,rand)
        if counta == 4:
            print(f"Correct, {counta}A{countb}B, Congratulations!")
            break
        else:
            print (f"Sorry, your guess result is incorrect:{counta}A{countb}B, try again to make it 4A0B! ")
    count += 1