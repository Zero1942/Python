a = [1, 2, 3, 4, 5, 6]
for i in a :
    j = i + 1
    print(j)

print('-'*20)
print(i)

'''
打印结果：for循环加后面的 print 结果 
3
4
5
6
7
--------------------
6
原因后面的 print 没有缩进不属于 for 循环
'''


# range() 函数包前不包后
for i in range(1,11) :
    j = i + 1
    print(j)

print('-'*20)
print(i)
print(' '*20)

'''
2
3
4
5
6
7
8
9
10
11
--------------------
10
'''

# 自定义函数: 求梯形面积
def trapezoid_area(base_up, base_down, height):
    area = (base_up + base_down)*height/2
    print(area)

# 调用函数并传参
# 方法1： 顺序传参
trapezoid_area(5,6,3)

# 方法2： 指定参数
trapezoid_area(height=3,base_up=5,base_down=6)
     