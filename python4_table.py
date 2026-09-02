chapter 9
city=('天津')
address='皇后街303'
print(city)
print(address)
#三引号：多行字符串
info='''皇后街303
收件人：peter 
手机号：123456789
'''
info2="""皇后街303
收件人：peter 
手机号：123456789
"""
print(info)
print('-------------')
print(info2)
chapter 10
print('北京')
print('欢迎你 ')
print('-----------')
print('北京\n欢迎你')#遇到\n即换行，可以连续换多行
print('北\n京\n欢\n')
print('----------')
print('北京北京 \t欢迎你')
print('hello\toooo')#hello是五个字符，一个制位表有八个字符8-5=3
print('hellooooo')
print('老师说：\'好好学习，天天向上\'')
print('老师说\"好好学习，天天向上\"')
#原字符，使转义字符失效的符号r或者R
print(r'北\n京\n欢\n')
print(R'北\n京\n欢\n')
chapter 11
s=('HELLOWORLD')
print(s[0],s[-10])#表示的是同一个字符
print('北京欢迎你'[4])
print('北京欢迎你'[-1])
print('-----------------')
print(s[2:7])#正向的从2开始到7结束不包含7
print(s[-8:-3])#反向递减
print(s[:5])#默认N从0开始
print(s[5:])#M默认切到字符串的结尾
chapter 12
x=('2022年')
y='北京冬奥会'
print(x+y)#连接两个字符串
print(x*10)
print(10*x)
print('北京'in y)#True
print('上海'in y)#False
