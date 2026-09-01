chapter 5
num=987#默认是十进制，表示整数
num2=0b1010101#使用二进制表示整数
num3=0o756# 使用八进制表示整数
num4=0x87ABF#使用十六进制表示整数
print(num)
print(num2)
print(num3)
print(num4)
chapter 6
height=187.6#身高
print(height)
print(type(height)) #type()作用是查看height这个变量的数据类型
x=10
b=10.0
print('x的数值类型',type(x))
print('b的数值类型',type(b))
x=1.99E1413
print('科学计数法',x,'x的数据类型',type(x))
print(0.1+0.2)#不确定的尾 数问题 0.3000000000004
print(round(0.1+0.2,1))
chapter 7
x=123+ 456j
print('实数部分',x.real)
print('虚数部分',x.imag)
print(type(x))
y=22j
print(type(y))
chapter 8
x=True
print(x)
print(type(x))
print(x+10)#10相当于1+10
print(False+10)#相当于0+10
print('----------------')
print(bool(18))#测试一下整数18的布尔值 True
print(bool(0),bool(0.0))#False
#总结：非0的整数的布尔值 都是True
print(bool('北京欢迎你'))#True
print(bool(''))#False
#所有空字符串的布尔值都是False
print(bool(False))#False
print(bool(None))#False
