## 3wd1

### HTML知识回顾
- 标准格式牢记，可以复用。
```
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
```
- The `<!DOCTYPE html>` declaration defines this document to be HTML5
  The `<html>` element is the root element of an HTML page
  The `<head>` element contains meta information about the document
  The `<title>` element specifies a title for the document
  The `<body>` element contains the visible page content
  The `<h1>` element defines a large heading
  The `<p>` element defines a paragraph
- atom有插件，可以自动补充html。packages里搜autoclose-html，或者点击[here](https://github.com/mattberkowitz/autoclose-html)下载
- HTML Images Syntax
```
<img src="url" alt="some_text" style="width:width;height:height;">
```
- The action attribute defines the action to be performed when the form is submitted.
  The method attribute specifies the HTTP method (GET or POST) to be used when submitting the form data.
```
<form action="/action_page.php">
  First name:<br>
  <input type="text" value="Mickey"><br>
  Last name:<br>
  <input type="text" name="lastname" value="Mouse"><br><br>
  <input type="submit" value="Submit">
</form>
```

## 3wd2

### 文档阅读
- 路由
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```
- 调试模式
```
app.run(debug=True)
```
```
app.debug = True
app.run()
```
- 给静态文件生成 URL ，使用特殊的 static 端点名:
```
url_for('static', filename='style.css')
```
这个文件应该存储在文件系统上的 static/style.css




## 3wd3

### 参考作业
- 发现自己的问题，看文档不够注意细节，关键点没找到。
- 迷失在文档里，没有找到解决问题的办法。
- **想让HTML的表格按钮和起作用，就不要忘记action**
  ```
  <form align="center" action="/input" method="GET"></form>
  ```
  ```
  @app.route('/input')

  ```
- **想让flaskr的变量在html起作用，就别忘了渲染的时候加上变量。**
  ```
  return render_template('404.html', city=city)
  ```
  ```
  {% extends "index.html" %}
  {% block content %}
  <p align="center">{{ city }}不存在，请点击help查询帮助</p>
  {% endblock %}
  ```
- 问题：
  - 点击按钮后地址会变化，如何保持地址不变？ `action='/'`
  - `searchword = request.args.get('key', '')`如何理解？
  - Jinja2模板的格式是否也是空4格？ 空2格。

## 3wd4

### 看沥川直播
- 先想清楚自己要做什么，然后一步一步实现。
- 大妈评论，最好用英文注释，中文输入法有困扰，而且逻辑不符合。
- 时刻牢记目标导向，牢记MVP，逐步完善。
- 出问题多考虑逻辑关系，多print查错。


## 3wd5

### jinja2
- `render_template()`渲染模板。
- `{% extends "index.html" %}`继承
  `{% if xxx %}`              `{% endif %}`条件
  `{% for xxx in xxx %}`      `{% endfor %}`循环
  `{% block content %}`       `{% endblock %}`块
  `{{ value }}`值

## 3wd6

### 看API
- args
A MultiDict with the parsed contents of the query string. (The part in the URL after the question mark).
- get(key, default=None, type=None)
Return the default value if the requested data doesn’t exist. If type is provided and is a callable it should convert the value, return it or raise a ValueError if that is not possible. In this case the function will return the default as if the value was not found:
```
>>> d = TypeConversionDict(foo='42', bar='blub')
>>> d.get('foo', type=int)
42
>>> d.get('bar', -1, type=int)
-1
```
- class werkzeug.datastructures.MultiDict(mapping=None)
A MultiDict is a dictionary subclass customized to deal with multiple values for the same key which is for example used by the parsing functions in the wrappers. This is necessary because some HTML form elements pass multiple values for the same key.

MultiDict implements all standard dictionary methods. Internally, it saves all values for a key as a list, but the standard dict access methods will only return the first value for a key. If you want to gain access to the other values, too, you have to use the list methods as explained below.

Basic Usage:
```
>>> d = MultiDict([('a', 'b'), ('a', 'c')])
>>> d
MultiDict([('a', 'b'), ('a', 'c')])
>>> d['a']
'b'
>>> d.getlist('a')
['b', 'c']
>>> 'a' in d
True
```
-
