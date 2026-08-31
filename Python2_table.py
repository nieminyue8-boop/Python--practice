chapter 1
true='真'
True='真'#True是python中的保留字
chapter 2
import keyword
print(keyword.kwlist )
print(len(keyword .kwlist))#获取保留字的个数
chapter 3
luck_number=8#创建一个整形变量luck_number, 并赋值为8
my_name='谢康'#字符串类型的变量
print('luck_number的数据类型是什么',type(luck_number))#class 'int'
print('my_name','的幸运数字是',luck_number,sep='')
#python动态修改变量的数据类型，通过赋不同类型的值就可以直接修改
luck_number='北京欢迎你'
print(type(luck_number))#class 'str'
#python当中允许变量指向同一个值
no=number=1104#no与number都指向了1104这个整数值 
print(no,number)
print(id(no))#id查看对象的内存地址的
print(id(number))
chapter 4
pi=3.1415926#定义了一个变量
print(id(pi))
PI=3.1415926 #定义了一个常量
print(id(PI))
