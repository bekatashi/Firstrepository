# Magic methods 
# Dunder methods
# __init__ 
# служебные методы

# res = 2+2 #__add__
# print(res)

# class A(int):
#     pass
# obj = A()
# print(dir(obj))

# magic methods of comparison:

# __eq__(self,other) -> ==
# __ne__(self,other)-> !=
# __lt__(self,other)-> <
# __gt__(self,other)-> >
# __le__(self,other)-> <= 
# __ge__(self,other) -> >=

# class Word(str):
#     def __new__(cls,word):
#         word = word.split(' ')
#         word = ''.join(word)
#         return super().__new__(cls,word)
#     def __init__(self,word) -> None:
#         self.word = word
#     def __gt__(self,other:str)->bool:
#         print('dunder method "greate than" worked')
#         return len(self)>len(other)
#     def __lt__(self, other: str) -> bool:
#         print('salam')
#         return len(self)< len(other)
# word = Word('   jo hn  ')
# word2 = Word('hell')
# print(word)
# print(word<word2)
# word1 =Word('Tome')
# reult = word>word1
# print(reult)
# print(word1 < word)


# Конструктор -> __new__
# Инициализатор -> __init__
# Деструктор ->__del__

# class Converter(float):
#     def __new__(cls, x):
#         if x <34:
#             raise Exception('u stupid?')
#         return super().__new__(cls,x*x)

#     def __init__(self,x) -> None:
#         print(self,'!!')
#         self.x = x

# obj = Converter(35.12)
# print(obj.x)
# print(obj)

# class Human:
#     def __new__(cls,stroka):
#         return 'stroka '+stroka
        
#     def __init__(self,stroku) -> None:
#         self.stroka = stroku
    
# obj = Human('Salam')
# obj2=Human('omega')
# print(obj2)

# class Base:
#     def __init__(self, string) -> None:
#         self.string = string
    
#     def __repr__(self) -> str:
#         return f" Class {self.__class__}\n Object: {self.string}"

#     def __str__(self) -> str:
#         return f" Object: {self.string}"

# word = Base("Akayoshi")
# print(word)
# print(repr(word))

# __setitem__  __getitem__  __delitem__

# class Sifra(int):
#     def __new__(cls,number):
#         print('Vyzov new')
#         instance = super().__new__(cls)
#         if not 0<number<100:
#             raise ValueError('write a correct num u bastard')
#         return instance 
#     def __init__(self,number) -> None:
#         self.number = number 
    
#     def __add__(self, x) -> int:
#         print('__add__ is working')
#         return f'result:{self.number-x.number}'

# value = Sifra(12)
# value1 = Sifra(23)
# print(value+value1)

# __sub__-
# __mul__*
# __floordiv__//
# __div__/
# __mod__%

# class Students:
#     def __init__(self,points):
#         self.points  = points
#         self.avg_res = (points['math'] + points['history'] + points['literature'])//3
#     def __gt__(self,other):
#         print(self.avg_res, other.avg_res)
#         return self.avg_res > other.avg_res

# john = Students({"math":100,"history":78,"literature":89})
# jamie = Students({"math":90,"history":90,"literature":89})
# print(john>jamie)


# class Mylist(list):
#     def __init__(self,ls):
#         self.ls = ls
#     def __getitem__(self,index):
#         print(self.ls[index-1])


# x=Mylist([121,212,2332,23])
# x[1]
# x[2]
# x[0]

# class Dollar:
#    @staticmethod
#    def dollarize(num):
#     return '${:,.2f}'.format(num)


# class MoneyFmt():
#   def __init__(self,amount):
#     self.amount = amount
#   def __str__(self):
#     return '${:,.2f}'.format(self.amount)
#   def update(self,amount):
#     self.amount = amount
#   def __repr__(self):
#     return str(self.amount)
 
        
# obj = MoneyFmt(123443243.2233)
# print(obj)
# obj.update(12121232121.21)
# print(repr(obj))


list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
new_list=['shorter' if len(i)<=4 else 'longer' for i in list_name]
print(new_list)