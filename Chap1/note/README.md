## 构思

1. 实现输入指令key，输出对应的值value。
2. 思路，先把数据变成dictionaries，测试，之后搞定退出和帮助文档，测试，然后是记录数据，打印历史记录，测试，最后整理优化。
3. 难点：需要生成dictionaries，需要读取数据，需要记录history，需要想清楚循环的条件语句的逻辑关系。

## 1wd1今日收获：

- `open`打开文档流
- `readline()`，读取每一行，返回string
- `strip('\n')`，去除字符，返回string
- `split(',')`，分离字符串，返回list
- `h = {l[0]:l[1]}`，建立dictionaries
- for循环大法好，充分利用它，它不会累死，让它一直跑吧

## 1wd2今日收获：

- 使用`with open() as xxx`, 不需要关闭file
- `string.strip()`, 去掉某些字符串，返回str
- `string.split(',')`，根据()里的内容，分开字符串，返回array
- 创建dictionaries的方法：建立空dictionaries，`d = {}`, 然后再补充key 和d[key]

## 1wd3今日收获:

- 昨天对于空dicttionaries，补充key和d[key]的理解是不深刻的。
- 整个作业的最难点就在于认识到如何建立dict，就是一个用法：
```
d = {}
d[key] = value
```
并且活学活用，例如作业里的把list转变dict
```
d[data[0]] = data[1]
```
又例如作业里的保存天气值
```
history = {}
if city in d.keys():
    history[city] = d[city]
```

## 1wd4今日收获:
- `if __name__ == '__main__'`到底是什么鬼，在[Stackoverflow相关问题](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)中找到了答案。它是python编译器读原文件时，执行其中函数的。在执行前，要确定`__name__`的值，如果控制台输入的是`python3 x.py`，其中`x.py`中有`if __name__ == '__main__'`，则`__main__`相当于`x`，可以获得`__main__`外部和内部的全部函数和值。如果`x.py`中没有`if __name__ == '__main__'`，而是`x.py`中`import y'的y模块中有，那么`__main__`相当于`y`，但是无法获得`__main__`内部的函数和值。作用是保护程序中的主函数，不被其他模块`import`。
- 使用多个`def`和`if __name__ == '__main__'`来写查天气程序。保存天气值的问题又出现了，原来使用的新建`{}`然后循环，在拿出去当作函数调用时，却无法使用。只能转变方法用`list`的`append`函数来增加，然后继续通过循环来输出。
- 继续实践了昨天大妈的编程方法，及时`git commit`, 先让程序跑起来，然后丰富各个功能，小步迭代，逐步优化。让自己的github绿油油，及时代码质量暂时不高，也体现强度和韧性啊。
- 看到大妈的快捷缩写输入用的很high，于是查阅学习了。
```
$ git config --global alias.st status
$ git config --global alias.ci commit
$ git config --global alias.pu push
$ alias ll='ls -lG'
```

## 1wd7今日收获

1. 见贤思齐，学习[thxiami](https://github.com/thxiami/Py101-004)和[Vwan](https://github.com/Vwan/Py101-004)，能力不够就模仿，跟随。他们和教练一样都是我的老师。

2. 完善weather程序后，发现久违的git错误。原因不明，git push失败，所以尝试git pull。结果出现以下错误。
```
You have not concluded your merge (MERGE_HEAD exists).
Please, commit your changes before you can merge.
```
之后查找[stackoverflow](https://stackoverflow.com/questions/11646107/you-have-not-concluded-your-merge-merge-head-exists)找到解答。
不知原因造成冲突，`git merge --abort`取消即可解决冲突。

3. 完善的weather包括：
	3.1 

4. 在@vwan那里学到了，算法性能比较。使用timeit 模块比较两个方法的运行时间；使用cProfile or profile比较两个方法的内部调用情况。记录下来。
```
from timeit import timeit
t1=timeit(generate_random_r1,number=1000)
t2=timeit(generate_random_r2,number=1000)
print (f"R1 duration:{t1}")
print (f"R2 duration:{t2}")
```
```
import cProfile
cProfile.run("generate_random_r1()")
cProfile.run("generate_random_r2()")
```
5. 使用列表解析式。代码行短，运行快。\n
`[int(i) for i in str(randint(1,20))]` \n
[]为返回值，int(i)为[]中的各元素，for循环是条件。

6. RTFM,没有好好查文档，提了小白问题。记录一下。
	print(f"{num}"),其中print里为什么有f，ok，现成模板给你，见[文档](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)，恩，这个用法还有个学名叫[Formatted string literals](https://stackoverflow.com/questions/39081766/what-are-formatted-string-literals-in-python-3-6)，stackoverflow有完美的解释。
	```
	title = 'Mr.'
	name = 'Tom'
	msg_count = 3

	# This is explicit but complex
	print('Hello {title} {name}! You have {count} messages.'.format(title=title, name=name, count=count))

	# This is simple but implicit
	print('Hello %s %s! You have %d messages.'%(title, name, count))

	# This is both explicit and simple. PERFECT!
	print(f'Hello {title} {name}! You have {msg_count} messages.')

	```
7. 将列表组合成字符串。
	```
	num = random.sample(range(1,9),4)
	print(num)
	print (("").join(str(x) for x in num))
	```
	`("").join()`完美的方法







