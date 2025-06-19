# name='iTuring'
# print(f'hello{name}')

# print("Python Rust\n")
# print('Python\tRust')
# print()
# print("Python\nRust")

# msg1,msg2='hello world',' iTuring'
# print(f'{msg1.title()}\n{msg1.upper()}\n{msg1.lower()}')
# print(f'{msg2}\n{msg2.strip()}')#删除两端的空格
# print('fname.txt'.removesuffix('.txt'))
# print('http://www.ituring.com.cn'.removeprefix('http://'))

# print(1, 1_000_000,1.5)
# print(True,False)
# print(1+1,1.0+1.0 ,1 + 1.0)
# print(3**2, 3/ 2, 3//2,5%2)

# bikes=['trek','cannondale','redline','specialized']
# print(bikes)
# print(bikes[0])
# print(bikes[2],bikes[-1])

# bikes=['trek']
# bikes[0]='giant'
# print(bikes)

# bikes=[]
# bikes.append('redline')
# bikes.insert(0,'trek')
# print(bikes)

# bikes=['giant','trek','redline']
# bikes.pop(0)
# print(bikes.pop())
# print(bikes)

# bikes=['giant','trek','redline']
# del bikes[0]
# bikes.remove('trek')
# print(bikes)

# nums=[4,1,9,6,5]
# print(len(nums))
# print(sorted(nums))
# print(nums)
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)
# nums.reverse()
# print(nums)

# bikes=['trek','cannondale','redline','specialized']
# for bike in bikes:
#     print(bike.title()) 

# print(range(2))
# print(list(range(2)))

# squares=[]
# for value in range(1,11):
#     squares.append(value**2)

# squares_comp=[value**2 for value in range(1,11)]
# print(squares == squares_comp)
# print(squares)
# print(min(squares),max(squares),sum(squares))

# bikees=['trek','cannondale','redline','specialized']
# print(bikes[1:])
# print(bikes[:-1])
# print(bikes[1:3])
# bikes_copy=bikes[:]
# bikes_copy.reverse()
# print(bikes_copy)
# print(bikes)

# dimensions =(200,50)
# for value in dimensions:
#     print(value)
    
# dimensions=(300,100)
# print(dimensions)
# dimensions=100
# print(dimensions)

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()  # 调用A.show
        print("B")  # 打印B

w= B()
w.show()
class C(A):
    def show(self):
        super().show()  # 调用A.show
        print("C")

class D(B, C):
    def show(self):
        super().show()  # 按MRO顺序调用B.show → C.show → A.show

d = D()
d.show()
# 输出顺序：
# A
# C
# B



