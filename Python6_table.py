chapter 16
print(True and True)
print(True and False)
print(False and False)
print(False and True)
print('-'*40)
print(8>7 and 6>5)
print(8>7 and 6<5)
print(9<0 and 10/0)#False,10/0并没有运算，当第一个表达式的结果为False，直接得结果了，不会计算and右侧的表达式了
print('-'*40)
print(True or True)
print(True or False)
print(False or False)
print(False or True)
print('-'*40)
print(8>7 or 10/0)#左侧表达式结果为True时，右侧直接不运算
print(8<7 or 10>0)
print('-'*40)
print(not True)
print(not False)
print(not 8>7)
Chapter 17
print('安位与运算',12&8)
print('按位或运算',4|8)
print('按位异或运算',31^32)
print('按位取反运算',~123 )
print('左移位',2<<2)#8,表示2向左移动两位2*2*2
print('左移位',2<<3)#相当于2*2*2*2
print('右移位 ',8>>2)#八向右移动两位相当于8//2，4//2
print('右移位',-8>>2)
