chapter 17
s=0#s存储累加和
i=1#初始化变量
while i<11:#条件判断
    s+=i
    #语句块
    if s>20:
        print('累加和大于20的当前数是',i)
        break
    i+=1
print('----登录问题-----')
i=0#统计登录的次数
while i<3:
    user_name=input('您的用户名')
    pwd=input('您的密码')
    if user_name=='xk' and pwd=='666':
         print('系统真在登录，请稍后')
         break
    else:
        if i<2:
         print('用户名或者密码不正确您还有',2-i,'次登录机会')
    i+=1
else:
    print('三次均输入错误，三分钟后尝试'
chapter18
for i in 'hello':
    if i=='e':
        break
    print(i)
print('------用户名和密码-------')
for i in range(1,4):
    user_name=input('输入您的用户名')
    psw=input('您的密码')
    if user_name=='xk' and psw=='666':
        print('登录成功，请稍等')
        break
    else:
        if i<3:
            print('您的用户或者密码有误，您还有',3-i,'次机会')
else:
    print('三次均输入错误，等待三分钟')
