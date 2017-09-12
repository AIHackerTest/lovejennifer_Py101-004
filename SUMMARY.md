# Python 个人教程目录

## python3 的变化
 
- 算术运算默认是浮点数，变为整数需要`int()`，但是`int()`只会省去小数位，保留整数位，所以如果要四舍五入，就需要`round()`或`int(round())`。
- `print`改为`print ()`
- `input()`代替`raw_input()`
   - 如果想实现`print`后的输入不换行，python2是在`print "xxx",`，python3则是`print ("xxx", end = "")`
   - 根据`print`原型，`print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`
- `input`在python3中作为关键词，无法再充当变量名，所以需要替换。
   - 如果依然使用`input`做变量名，则会出现`'_io.TextIOWrapper' object is not callable`错误，即把input给覆盖成本地变量，无法实现`input`的原本功能。


