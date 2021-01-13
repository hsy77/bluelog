在动态Web程序中，视图函数返回的HTML数据往往需要根据相应的变量（比如查询参数）动态生成。当HTML代码保存到单独的文件中时，我们没法再使用字符串格式化或拼接字符串的方式来在HTML代码中插入变量，这时我们需要使用模板引擎（templateengine）。借助模板引擎，我们可以在HTML文件中使用特殊的语法来标记出变量，这类包含固定内容和动态部分的可重用文件称为模板（template）。

Flask默认使用的模板引擎是Jinja2，它是一个功能齐全的Python模板引擎，除了设置变量，还允许我们在模板中添加if判断，执行for迭代，调用函数等，以各种方式控制模板的输出。对于Jinja2来说，模板可以是任何格式的纯文本文件，比如HTML、XML、CSV、La TeX等。在这一章，我们会学习Jinja2模板引擎的基本用法和一些常用技巧。

比如if判断、for循环等：[插图]

​	`{%...%}`

（2）表达式比如字符串、变量、函数调用等：[插图]

`{{...}}`

（3）注释[插图]

`{#...#}`

Jinja2支持使用“.”获取变量的属性，比如user字典中的username键值通过“.”获取，即user.username，在效果上等同于user['username']。

Jinja2允许你在模板中使用大部分Python对象，比如字符串、列表、字典、元组、整型、浮点型、布尔值。它支持基本的运算符号（+、-、*、/等）、比较符号（比如==、!=等）、逻辑符号（and、or、not和括号）以及in、is、None和布尔值（True、False）。



在这个If语句里，如果user.bio已经定义，就渲染{% if user.bio%}和{% else %}之间的内容，否则就渲染{% else %}和{% endif%}之间的默认内容。末尾的{% endif %}用来声明if语句的结束，这一行不能省略。

![image-20210111185849188](C:\Users\rain\AppData\Roaming\Typora\typora-user-images\image-20210111185849188.png)

![image-20210111185955683](C:\Users\rain\AppData\Roaming\Typora\typora-user-images\image-20210111185955683.png)



Flask还提供了一个render_template_string()函数用来渲染模板字符串。其他类型的变量通过相同的方式传入。传入Jinja2中的变量值可以是字符串、列表和字典，也可以是函数、类和类实例，这完全取决于你在视图函数传入的值。下面是一些示例：

![image-20210111190112000](C:\Users\rain\AppData\Roaming\Typora\typora-user-images\image-20210111190112000.png)

如果你想传入函数在模板中调用，那么需要传入函数对象本身，而不是函数调用（函数的返回值），所以仅写出函数名称即可。当把函数传入模板后，我们可以像在Python脚本中一样通过添加括号的方式调用，而且你也可以在括号中传入参数。



除了渲染时传入变量，你也可以在模板中定义变量，使用set标签：

<img src="C:\Users\rain\AppData\Roaming\Typora\typora-user-images\image-20210111190241686.png" alt="image-20210111190241686" style="zoom:80%;" />

如果多个模板都需要使用同一变量，那么比起在多个视图函数中重复传入，更好的方法是能够设置一个模板全局变量。Flask提供了一个app.context_processor装饰器，可以用来注册模板上下文处理函数，它可以帮我们完成统一传入变量的工作。模板上下文处理函数需要返回一个包含变量键值对的字典，如代码清单3-3所示。

![image-20210111190715035](C:\Users\rain\AppData\Roaming\Typora\typora-user-images\image-20210111190715035.png)

除了使用app.context_processor装饰器，也可以直接将其作为方法调用，传入模板上下文处理函数：

![image-20210111190737633](C:\Users\rain\AppData\Roaming\Typora\typora-user-images\image-20210111190737633.png)

url_for()用来获取URL，用法和在Python脚本中相同。在前面给出的watchlist.html模板中，用来返回主页的链接直接写出。在实际的代码中，这个URL使用url_for()生成，传入index视图的端点：

![image-20210111190918942](C:\Users\rain\AppData\Roaming\Typora\typora-user-images\image-20210111190918942.png)



过滤器（filter）是一些可以用来修改和过滤变量值的特殊函数，过滤器和变量用一个竖线（管道符号）隔开，需要参数的过滤器可以像函数一样使用括号传递。下面是一个对name变量使用title过滤器的例子：

![image-20210111191311559](C:\Users\rain\AppData\Roaming\Typora\typora-user-images\image-20210111191311559.png)

这会将name变量的值标题化，相当于在Python里调用name.title()。再比如，我们在本章开始的示例模板watchlist.html中使用length获取movies列表的长度，类似于在Python中调用len(movies)：

另一种用法是将过滤器作用于一部分模板数据，使用filter标签和endfilter标签声明开始和结束。比如，下面使用upper过滤器将一段文字转换为大写：

![image-20210111191354720](C:\Users\rain\AppData\Roaming\Typora\typora-user-images\image-20210111191354720.png)

另外，过滤器可以叠加使用，下面的示例为name变量设置默认值，并将其标题化：

![image-20210111191435295](C:\Users\rain\AppData\Roaming\Typora\typora-user-images\image-20210111191435295.png)

我们使用include标签来插入一个局部模板，这会把局部模板的全部内容插在使用include标签的位置。比如，在其他模板中，我们可以在任意位置使用下面的代码插入_banner.html的内容：

![image-20210111192333824](C:\Users\rain\AppData\Roaming\Typora\typora-user-images\image-20210111192333824.png)

块的开始和结束分别使用block和endblock标签声明，而且块之间可以嵌套。在这个基模板中，我们创建了六个块：head、title、styles、content、footer和scripts，分别用来划分不同的代码。

在运行前两章的示例程序时，我们经常在命令行看到一条404状态的GET请求记录，请求的URL为/favicon.ico，如下所示：

这个favicon.ico文件指的是Favicon（favorite icon，收藏夹头像/网站头像），又称为shortcut icon、tab icon、website icon或是bookmark icon。顾名思义，这是一个在浏览器标签页、地址栏和书签收藏夹等处显示的小图标，作为网站的特殊标记。浏览器在发起请求时，会自动向根目录请求这个文件，

![image-20210111202954708](C:\Users\rain\AppData\Roaming\Typora\typora-user-images\image-20210111202954708.png)