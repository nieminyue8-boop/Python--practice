chapter 1
a=100# 变量a,值为100
b=50# 变量b,值为50
print(90)
print(a)#输出变量的值,a的值是100
print(a*b)#输出a*b的运算结果,运算结果为5000
print('北京欢迎你！')
print("北京欢迎你！")
print('''北京欢迎你！''')
x=999999
b=999999
print(x*b)
chapter 2
a=100
b=50
print(a,b,'要么出众，要么出局！！！ ',sep='6')
chapter 3
print('b')
print(chr(98))
print('C')
print(chr(67))
print(8)
print(chr(56))
print('[')
print(chr(91))
chapter 4
print(ord('北'))
print(ord('京'))
print(chr(21271),chr(20140))
chapter 5
print('北京',end='--.')
print('欢迎你') #没有修改结束符，所以在Print之后会有一个空行
print('xi')
print('我喜欢你',end='0')
print('谢康')
chapter 6
print('北京欢迎你'+'2026')
chapter 7
name=input('我的名字是')
print('我的性名字是：'+name)
chapter 8
#要球从键盘输入年份，，要求是4位的年份，举例：1990
year=input('请输入您的出生年份：')
year=input('请输入您的出生年份：')#要球从键盘输入年份，，要求是4位的年份，举例：1990
chapter 9
#coding=utf-8
#中文声名注释一定写在第一行
'''
版权所有：谢康派森信息技术工作
文件名：示例2-11多行注释
创始人：谢康
'''
"""
版权所有：谢康派森信息技术工作
文件名：示例2-11多行注释
创始人：谢康
"""
print('hello')
chapter 10
#一般代码不需要缩进的
print('hello ')
print('world')
#类的定义
class Student:
    pass
#函数的定义
def fun: 
    pass
chapter 11
p=open('note.txt','w')#打开文件w-->write
print('北京欢迎 ',file=p)#将“北京欢迎你“ 输出(写入）到note.txt文件中
p.close()#关闭文件
chapter 12
num=input('请输入您的新运数字 ：')
print('您的幸运数字是:'+num)#连接成公说明num是字符串类型
sorry=input('how long',)
sorry=int(sorry)
print('您的幸运数字示：',sorry)
peter=input('peterage')
peter=int(peter)
print('peterage',peter)
exam 1
p=open('text.txt','w')
print("",file=p)
p.close()
exam 2
name=input('姓名')
name=int(name)
age=input('年龄')
love=input('座右铭')
print('---------自我介绍---------')
print('姓名：',name)
print('年龄：'+age)
print('座右铭：'+love)

dog=input('谁是周治愈的儿子')
print('谁是周治愈的儿子',dog)

