chapter 13
#初始化变量
i=0
while i<3:#条件判断
    #语句块
    user_name=input('请输入您的用户名')
    pwd=input('请输入密码')
    if user_name=='xk' and pwd=='666':
        print('系统正在登录，请稍后')
        #需要改变怒换变量，目的：推出循环
        i=8#第三行，判断i<3, 8<3 False 推出while循环（改变变量）
    else:
        if i<2:
            print('用户名或者密码不正确，您还有',2-i,'次机会')
        i+=1# i=i+1（改变变量）
#单分支的判断
if i==3:#当用户名或者密码输入三次不正确的时候，循环结束了，i最大值为3
    print('对不起，三次均输入错误')

for i in range(1,4):
    user_name=input('请输入您的用户名')
    psw=input('请输入您的密码')
    if user_name=='zzy' and psw=='777':
        print('正在登录中')
        break
    else:
        if i<3:
            print('您还有',3-i,'次机会')
else:
   print('稍等三分钟登录，您已尝试三次')
chapter 14
#三行四列
for i in range(1,4):#外层循环控制的是行数
    for j in range(1,5):#内层循环控制的是列数
        print('*',end='')
    print()#空的print语句，作用是换行
print('------直角三角形-------')
for i in range(1,6):
    #*的个数与行数相同，range（1，2）
    for j in range(1,i+1):
        print('*',end='')
    print()
