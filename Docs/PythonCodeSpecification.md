# Python code specification

The acticle introduction of Python comment...

- 项目：首字母大写+大写式驼峰, 如：ProjectName；
- 包：使用小写字母命名。多个单词之间用下划线分隔。
- 模块：使用小写字母命名。多个单词之间用下划线分隔。
- 类/异常（驼峰命名法）：首字母大写+大写式驼峰。Python中一个模块可以包含多个类。私有类名称需要以下划线开头。如：HelloWorld 或 _HelloWorld；
- 函数：使用小写字母命名。多个单词之间用下划线分隔。私有函数名称需要以下划线开头。
- 变量：使用小写字母命名。多个单词之间用下划线分隔。私有变量名称需要以下划线开头。
- 常量/全局变量：使用大写字母命名。多个单词之间用下划线分隔。私有常量名称需要以下划线开头。

## Single line and mulity line comment
### Single line comment
```python
# This is a single line comment...
```
### Mulity line comment
```python
"""
This is a mulity line comment, use double quotation marks!
But you can use singgle quatation marks.
"""
```