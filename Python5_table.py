chapeter 12
x=10
y=3
z=x/y#在执行除法运算的时候，将运行结果赋值给z
print(z,type(z))#隐式转换，通过运算隐式转了结果类型
#float类型转换成int类型，只保留整数部分
print('float类型转换成int类型:',int(3.14))
print('float类型转换成int类型:',int(3.9))
print('float类型转换成int类型:',int(-3.14))
print('float类型转换成int类型:',int(-3.9))
#将int转成float类型
print('将int转成float类型:',float(10))
#将str转成int类型
print(int('100')+int('200'))
#将字符串转成int或者float报错的情况
#print(int('18a'))#value error
#print(int('3.14'))
#print(float('45a.123'))

#chr()ord()一对
print(ord('杨'))
print(chr(26472))
#进制之间的转换操作，十进制与其他进制之间的转换
print('十进制转换成十六进制：',hex(26472))
print('十进制转换成八进制：',oct(26472))
print('十进制转换成二进制：',bin(26472))
chapter 13
s='3.14+3'
print(s,type(s))
x=eval(s)#使用eval函数去掉s这个字符串中左右的引号，执行了加法运算
print(x,type(x))
print(round(x,3))
#eval函数经常与input函数一起使用，用来获取用户输入的数值
age=eval(input('请输入您的年龄：'))#将字符串类型转换成int类型，相当于int（age）
print(age,type(age))
height=eval(input('请输入您的身高'))
print(height,type(height))
hello='北京欢迎你'
print('hello')
print(eval(hello))#输出了北京欢迎你
print(eval('北京欢迎你'))
chapter 14
x=20#直接赋值，直接将20赋值给左侧的变量x
y=10
x=x+y#将x+y的和赋值给x，x的值为30
print(x)#x的值为30
x+=y#40，相当于x=x+y
x-=y#相当于x=x-y
print(x)#30
x*=y
print(x)
x/=y
print(x)#30.0发生了类型转换x的数据类型为float类型
print(type(x))
x%=2#相当于x=x%2
print(x)#0.0
z=3
y//=z#y=y//z
print(y)
y**=2#y=y**2
print(y)
#python支持链式赋值
a=b=c=100#相当于执行了a=100 b=100 c=100
print(a,b,c,)
#python支持系列解包赋值
a,b=10,20#相当于执行了a=10，b=20
print(a,b)
print('-------如何交换两个变量的值呢？-----------')
a,b=b,a#将b的值给a，将a的值给b
print(a,b)
chapter 15
print('98大于90吗',98>90)
print('98小于90吗',98<90)
print('98等于90吗',98==90)
print('98不等于90吗',98!=90)
print('98大于等于98吗',98>=98 )
print('98小于等于90吗',98<=98 )
