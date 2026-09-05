chapter 1
#赋值运算符的顺序是从右到左
name='张三'
age=20#链式赋值
a=b=c=d=100#字符串分解赋值
a,b,c,d='room'
print(a)
print(b)
print(c)
print(d)
print('--------输入输出语句也是典型的顺序结构----------')
name=input('您的姓名')
age=eval(input('请输入您的年龄'))
luck_number=eval(input('请输入您的幸运数字'))
print('姓名',name)
print('年龄',age)
print('幸运数字',luck_number)
print(age)
chapter 2
number=eval(input('请输入您的6位中奖号码'))
#使用if语句
if number==7777: #等值判断
    print('恭喜您，中奖了')
if number!=7777:
    print('您未中本期大奖')
print('------以上if判断的表达式，是通过比较运算符计算出来的，结果是布尔类型----')
n=7#赋值操作
if n%2:#98%2的余数为0，0的布尔值是False，非0的布尔值为True
    print(n,'是奇数')#由于98%2的值为0，所以该行代码不会执行
if not n%2:#98%2的余数是0的布尔值为false，not false 就为True
    print(n,'偶数')
print('------判断一个字符串是否是空字符串--------')
x=input('请输入一个字符串')
if x:  #python中一切皆对象，每一个对象都有一个布尔值，而非空字符串的布尔值为True，空字符串的布尔值为False
    print('x是一个非空字符串')
if not x:#空字符串的布尔值为False，not x 为True
    print('x是一个空字符串')
print('-------表达式也可以是一个单纯的布尔型变量--------')
flag=eval(input('请输入一个布尔类型的值：True或False'))
if flag:
    print('flag的值为True')
if not flag:
    print('flag的值为False')
print('------使用if语句时 ，如果语句块中z还有一句代码，可以将语句块直接写在：的后面----')
a=5
b=10
if a>b:max=a#语句块只有一句赋最大值
print('a和b的最大值',max)
