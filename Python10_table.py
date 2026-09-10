chapter 11
#初始化变量
answer=input('今天要上课吗y/n')
while answer=='y':#条件判断
    print('好好学习，天天向上')#语句块
    #改变变量
    answer = input('今天要上课吗y/n')
#1-100之间的累加和
s=0#存储累加和
i=1#初始化变量
while i<=100:#条件判断
    s+=i#语句块
    #改变变量
    i+=1#相当于i=i+1
print('1-100之间的累加和',s)
chapter 12
#1-100之间的累加和
s=0#存储累加和
i=1#初始化变量
while i<=100:#条件判断
    s+=i#语句块
    #改变变量
    i+=1#相当于i=i+1
else:
    print('1-100之间的累加和',s)
pwd='密码'
while pwd !='123456' :
    pwd=input('您的密码是')
print('密码正确')
