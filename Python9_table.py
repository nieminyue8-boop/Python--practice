chapter 5
anwser=input('请问您，喝酒了吗')
if anwser=='y':#answer的值为y表示喝酒了
    proof=eval(input('请输入酒精含量'))
    if proof<20:
        print('构不成酒驾，祝您一路平安')
    elif proof<80:#20<=proof<80
        print('已构成酒驾请不要开车')
    else:
        print('已达到醉驾标准，请千万不要开车')
else:
    print('你走吧没你啥事')
 chapter 6
user_name=input('请输入您的用户名')
pwd=eval(input('请输入您的密码'))
if user_name=='xk'and pwd==666:
    print('登录成功')
else:
    print('用户名或者密码不正确')
