## 2wd2
- API是什么？
  - Application Programming Interface (应用编程接口)
  - API就是餐厅的服务员，连接顾客和厨房里美食的连接者。
  - 请求它，就可以访问它的数据，使用它的功能。
  - 它返回的数据稍加处理，就可以实现我们想实现的目的。

- 如何安装requests模块?
```
$ pip install requests
```
  如果已经安装anaconda，则无需再次安装requests模块。

- 如何在程序中引入 requests 模块？
```
import requests
```

- 如何使用 requests 模块发送请求？
```
r = requests.get('https://api.github.com/events')
```
```
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
```

- POST 和 GET 是什么意思？
  - GET: 从指定的资源请求数据。
  - POST: 向指定的资源提交要被处理的数据

- 今日完成了基础作业，模范demo，试出答案。

## 2wd3

### 第一次参加线下Pair Programming

#### 我的收获

- 复盘了作业的基础版本，发现了很多自己的诸多漏洞。
模仿知心天气API的python demo时，没有注意函数参数的格式。其实第一次写作业的时候是复制粘贴，今天结对复盘的时候，想当然的凭记忆和下意识写，结果出错很多，其中包括：字典格式为`{a: b}`，不是自己第一映像中的`{a = b}`。是`'unit': 'c'`，而不是`'unit': c`。
- CH2的最基本要求就是找到API，`import requests`，然后用requests的get方法，获得json对象，通过`import json`使用`json.text`，可以打印出json格式的内容。但是即使可以打印出来，依然不是python可以直接用的格式(因为我试了，报错显示json格式不能执行我所做针对字典的操作)，需要把json格式转换成字典格式。使用`jason.loads()`方法，得到可以用的格式。然后根据API示例显示，json格式是字典套列表再套字典再套字典的格式，`{'a':[{'b':{'c':'d'}, 'e'}]}`，相对应的字典也相同。就逐个读取，拿到想要的元素，然后`print`出来。
其中同伴的做法和我不同，他根本不需要`import json`，直接`requests.get().json()`即可，简单易用，这应该是requests模块中特有的方法。
- 之后的代码就是CH1中的内容，这次线下结对也暴露了自己CH1作业中的问题，思路是混乱的，实现MVP的想法很快忘记。只是靠回忆背诵自己之前的代码，而不是真正掌握。原因是之前的代码中有关history的部分是借鉴别人的，脑海中没有透彻理解，那么就很难熟练复盘出来。

#### 我的感想

- 这是第一次有人看着我写代码，而且还是两位。有一些紧张，最开始写代码是完全没有思路的。之后频出bug，不停地改错。都是细节，细节是魔鬼。少个字母，少个冒号，少个逗号，少个引号，缩进错误...
- 让自己对于自己所写的代码逻辑更清晰，旁人盯着看的压力逼得自己不得不思路更清晰。面对同伴的疑问逼得自己深入思考，能做到给别人讲清楚讲明白的地步才可以。
- 最后听到俊宇@Wangjunyu关于环境变量配置的入坑分享，收获很多。坑的出现往往取决于自己的好奇心，想试试新鲜工具，势必会碰到许多坑。而面对坑不能退缩，就是干，就是要克服，办法总比困难多。

#### 俊宇教练分享后自己所吸收的东西

- 首先是debug的方法。这一行上下都加print，看看程序有没有走到这一步，缩小范围定位后开始研究为何出错。
- 其次是环境变量的探讨。环境变量通常是安装程序自动配置好的，但是也有一些情况需要手动配置，在Google上询问，然后输入指令，在正确的位置写入环境变量。环境变量见是靠:做分隔的。越靠前的环境变量越有优先级。
- 对新工具有问题要先查看本工具自带的帮助文档，往往更快更有效，不要一上来就google。使用控制台显示帮助文档查询`prenv -h`或者`man python`等方法。
- 要对Shell脚本有基本的了解，不仅能深入理解软件安装的坑，还能更好理解控制台报错信息，当然会大大提升编程效率。例如`pip show requests | cat > ~/Desktop/ttt.txt`把pip中的requests详情导入桌面的ttt.txt文件中，`pip show requests | grep License`在pip中的requests中查询有没有License信息。管道，重定向，查询，正则表达式。恩，很多很多都需要自己一一去了解。

## 2wd4

- 如何获得 API 返回的数据？
  用get或post方法申请后，会返回json对象，此时`import json`，用'json.text'即可以获得 API 返回的数据。
- 如何在 Python 中处理 JSON 数据？
```
import json

text = json.loads(rtn) # rtn 为 API 返回的数据

temperature = text['results'][0]['now']['temperature']
```
- JSON 的来历是什么？ 为什么绝大多数 API 都选择以 JSON 的方式传递数据？
  - JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。 易于人阅读和编写。同时也易于机器解析和生成。JSON建构于两种结构：“名称/值”对的集合（A collection of name/value pairs）和值的有序列表（An ordered list of values），这两种数据格式在几乎所有的编程语言中都存在，这使得一种数据格式在同样基于这些结构的编程语言之间交换成为可能。

## 2wd5

- 完成进阶作业，自己想复杂，把API中的 start 和 days 参数都写入作业中，但是发现无数的if循环嵌套让自己苦不堪言，无法突破，最后才放弃额外的两个参数。看到沥川简单易懂的直接让input的值等于0，1，2就轻松解决问题，我茅塞顿开，然后才完成了作业。
- 实现进阶作业后的收获：
  - 对于`append()`方法和for循环更加熟悉。最基础的遍历列表一定要熟练，多练习。
  - 全局变量和局部变量一定要考虑清楚，报错只要出现`UnboundLocalError: local variable 'unit' referenced before assignment` 那就是全局变量和局部变量的问题，不要想当然地认为你定义的变量在任何地方都可以用。
- 看一下卡片上对于股票查询软件的讲解，让自己思路更加清晰了，以下记录一些笔记。
  - 第一步，打开并读取这个文件，用print测试一下。
  ```
  with open('xxx.txt', 'r', encoding = 'utf-8')as f:
      for line in readlines():
          print(line)

  ```
    然后实现最小MVP,立刻git记录V0.1版本。
  - 终端输入`vi xxx.txt`以在终端打开文件，显示文件内容。输入:q 退出。
  - 第二步，用`line.split(',')`把文件中的内容通过 , 分隔，返回列表。继续`git commit -m "split"`记录，可以输入一些提示语言。
  - 第三步，用`dict.update()`方法把循环后的多个list转化成一个dict。继续git记录V0.2版本。
    查询后发现update用法：
  ```
  #!/usr/bin/python3
  dict = {'Name': 'Maxsu', 'Age': 7}
  dict2 = {'Sex': 'female' }
  dict.update(dict2)
  print ("updated dict : ", dict)
  ```
  ```
  updated dict : {'Sex': 'female', 'Age': 7, 'Name': 'Maxsu'}
  ```
  - 第四步，`input()`接受用户输入，然后设置空dict，{}，之后使用`dict.get()`方法来查找输入值所对应的值。继续git记录V0.3版本。网络上查了get用法。
  `dict.get(key, default=None)`,对于键(key)存在则返回其对应值，如果键不在字典中，则返回默认值。
  - 第五步，使用`if..else`分支语句给出提示，然后优化输出内容。继续git记录优化版本V1.1。
  - 第六步，设置空list，[]，之后使用`list.append()`方法返回历史。继续git记录优化版本V1.2。
  - 第七步，加入while循环，`while True`不是`while true`，注意缩进，可以用tab键，循环在input之外，通过break终止循环。继续git记录优化版本V1.3。

## 2wd7

### 重做CH1的作业，虽然做了3遍了，但按照卡片上的教程，是新的实现方法，但还是会遇到问题：
  - 地址要加`" "`，不是直接赋值的。。。
  ```
  PATH = "../resource/weather_info.txt"
  ```
  - update函数直接返回调用它的字典，根本不用重新新建返回值。
  以下ok
  ```
  dict.update({xx : yy})
  ```
  以下不ok
  ```
  d = dict.update({xx : yy})
  ```
  - 完成MVP，要先确定`if...else`，之后再添加附加功能`elif`

### 安装pyenv

  - 认真读帮助文档真是个好习惯，不按文档的方法做就必然会出错。
  - 安装最好是`git clone`, `brew install`没有更新新版本。
  - 环境变量一个一个输入，输入完记得重启控制台。
    不放心可以打开bash_file瞅瞅，别乱删就行。
  ```
  $ open ~/.bash_profile
  ```
    打开后有关pyenv的在最下方，注释可以加。环境变量是从下往上读取的。[某博文](http://debugtalk.com/post/use-pyenv-manage-multiple-python-virtualenvs/)
  ```
  # pyenv
  export PYENV_ROOT="$HOME/.pyenv"
  export PATH="$PYENV_ROOT/bin:$PATH"
  eval "$(pyenv init -)"
  ```
  - 要记住好习惯，安装好后第一时间就是看帮助文档。
  ```
  $ pyenv -h
  ```
  - 查看可安装的Python版本
  ```
  $ pyenv install --list
  ```
  - 安装所需要的python版本就好了
  ```
  $ pyenv install 3.6.2
  $ pyenv install 2.7.13
  ```
  - 查看当前系统中所有可用的Python版本
  ```
  $ pyenv versions
  * system (set by /Users/Lilongshen/.pyenv/version)
  2.7.13
  3.6.2
  ```
  - 切换Python版本
  ```
  $ pyenv global 2.7.13
  ```
  - 最后检验是否已经切换
  ```
  $ python
  Python 2.7.13 (default, Aug 27 2017, 18:21:01)
  [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>>
  ```
  
