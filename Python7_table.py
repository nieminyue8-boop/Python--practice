chapter 3
number=eval(input('请输入您的6位中奖号码'))
#if-else结构
if number==666:
    print('恭喜您中奖了')
else:
    print('您未中本期大奖 ')
print('----以上代码可以使用条件表达式进行简化-----')
result='恭喜您中奖了' if number==666 else'您未中奖'
print(result)
print('恭喜您中奖了' if number==666 else'您未中奖')
chapter 4
score=eval(input('请输入您的成绩'))
#多分支结构
if score<0 or score>100:
    print('成绩有误')
elif 0<=score<60:
    print('E')
elif score<70:
    print('D')
elif 70<=score<80:
    print('C')
elif 80<=score<90:
    print('B')
else:
    print('A')
