# Python Develop Memo

#### Python介绍
* Python由荷兰数学和计算机科学研究学会的吉多·范罗苏姆于1990年代初设计，作为一门叫做ABC语言的替代品。Python提供了高效的高级数据结构，还能简单有效地面向对象编程。Python语法和动态类型，以及解释型语言的本质，使它成为多数平台上写脚本和快速开发应用的编程语言，随着版本的不断更新和语言新功能的添加，逐渐被用于独立的、大型项目的开发。
* Python解释器易于扩展，可以使用C语言或C++（或者其他可以通过C调用的语言）扩展新的功能和数据类型。Python也可用于可定制化软件中的扩展程序语言。Python丰富的标准库，提供了适用于各个主要系统平台的源码或机器码。

#### Python基本语法
* Python的设计目标之一是让代码具备高度的可阅读性。它设计时尽量使用其它语言经常使用的标点符号和英文单字，让代码看起来整洁美观。它不像其他的静态语言如C、Pascal那样需要重复书写声明语句，也不像它们的语法那样经常有特殊情况和意外。
* Python开发者有意让违反了缩进规则的程序不能通过编译，以此来强制程序员养成良好的编程习惯。并且Python语言利用缩进表示语句块的开始和退出（Off-side规则），而非使用花括号或者某种关键字。增加缩进表示语句块的开始，而减少缩进则表示语句块的退出。缩进成为了语法的一部分。例如if语句：python3

<pre>
    <code>
    age = int(input("请输入你的年龄: "))

    if age < 21:

    &ensp;&ensp;&ensp;&ensp;print("你不能买酒。")

    &ensp;&ensp;&ensp;&ensp;print("不过你能买口香糖。")

    print("这句话在if语句块的外面。")
    </code>
</pre>

#### Python控制语句
* <b>if语句</b>，当条件成立时运行语句块。经常与else，elif（相当于else if）配合使用，称为if-elif-else语句。
* <b>for语句</b>，遍历列表、字符串、字典、集合等迭代器（容器），依次处理迭代器中的每个元素。有时和else连用，称为for-else语句。
* <b>while语句</b>，当条件为真时，循环运行语句块。有时和else配合使用，称为while-else语句。
* <b>try语句</b>，必与except配合使用处理在程序运行中出现的异常情况，称为try-except语句。常与else，finally配合使用，称为try-except-else语句，try-except-finally语句，try-except-else-finally语句
* <b>class语句</b>，用于定义类型。
* <b>def语句</b>，用于定义函数和类型的方法。
* <b>pass语句</b>，表示此行为空，不运行任何操作。
* <b>assert语句</b>，用于程序调试阶段时测试运行条件是否满足。
* <b>with语句</b>，Python2.6以后定义的语法，在一个场景中运行语句块。比如，运行语句块前加密，然后在语句块运行退出后解密。
* <b>yield语句</b>，在迭代器函数内使用，用于返回一个元素。自从Python 2.5版本以后。这个语句变成一个运算符。
* <b>raise语句</b>，制造一个错误。
* <b>import语句</b>，导入一个模块或包。
* <b>from…import语句</b>，从包导入模块或从模块导入某个对象。
* <b>import…as语句</b>，将导入的对象赋值给一个变量。
* <b>in语句</b>，判断一个对象是否在一个字符串/列表/元组里。

#### 参与贡献

1.  GF Fork 本仓库
2.  GF 新建 Feat_xxx 分支
3.  GF 提交代码
4.  GF 新建 Pull Request

#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
