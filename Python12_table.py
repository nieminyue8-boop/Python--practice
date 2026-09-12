chapter 15
print('-----倒三角形-----')
for i in range(1,6):
    for j in range(1,7-i):
        print('*',end='')
    print()
print('-----等腰三角形-----')
'''
&&&&*
&&&***
&&*****
&*******
*********
'''
for i in range(1,6):
    #倒三角形
    for j in range(1,6-i):
        print(' ', end='')
    for k in range(1,2*i):
        print('*',end='')
    print()#当两个for循环结束后再换行
chapter 16
row=eval(input('棱形的行数'))
while row%2==0:#判断行数的奇偶性，行数是偶数要重新输入行数
    print('重新输入棱形的行数')
    row = eval(input('输入棱形的行数'))
#输出棱形
top_row=(row+1)//2#上半部分的行数
#上半部分
for i in range(1,top_row+1):
    #倒三角形
    for j in range(1,top_row-i+1):
        print(' ', end='')
    for k in range(1,2*i):
        print('*',end='')
    print()#当两个for循环结束后再换行
#棱形的下半部分
row_bottom=row-top_row
for i in range(1,row_bottom+1):
    #直角三角形
    for j in range(1,i+1):
        print(' ', end='')
    #倒三角形
    for k in range(1,2*row_bottom-2*i+2):#1-->range(1,6),2-->(1,4),1-->(1,2)
        print('*',end='')
    print()
