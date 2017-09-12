# 模仿教练在卡片中的代码，和编程方式。

dic = {}
history = []
PATH = "../resource/weather_info.txt"

def read_file():
    with open(PATH, "r") as f:
        for line in f.readlines():
            #print(line)
            line_list = line.split(',')
            #print(line_list)
            dic.update({line_list[0]: line_list[1]})
    return dic

def search():
    while True:
        city = input("请输入指令或城市名: ")
        d = read_file()
        if d.get(city):
            w = f'{city}的天气为: {d.get(city)}'
            print(w)
            history.append(w)
        elif city in ['help', 'h']:
            print('This is help doc.')
        elif city == 'history':
            for info in history:
                print(info)
        elif city in ['q', 'quit', 'exit']:
            break
        else:
            print(f'找不到{city}，请重新输入')

if __name__ == '__main__':
    search()
