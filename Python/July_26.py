# class Person:
#     cls_name = 'Person'
    
#     def __init__(self, name, job, birth, contry):
#         self.name = name
#         self.job = job
#         self.birth = birth
#         self.contry = contry
    
#     def rap(self):
#         print(f'{self.name}가 랩을 합니다.')

#     def dance(self):
#         print(f'{self.name}가 춤을 춥니다.')

#     def cow(self):
#         return print(f'{self.name}가 소몰이를 합니다.')

#     @classmethod
#     def class_method(cls):
#         print(f'{cls.cls_name}의 클래스 메서드를 호출했습니다.')

#     @staticmethod
#     def static_method(a, b):
#         print(a + b)

#     def __str__(self):
#         return f'{self.name} 의 매직 메서드를 호출했습니다.'

    
#     def cow2():
#         print('사실 소몰이 창법입니다.')

# iu = Person('iu', '가수', '1993년 5월 16일', '대한민국')

# print(f'직업 : {iu.job}')
# print(f'생년월일 : {iu.birth}')
# print(f'국적 : {iu.contry}')

# iu.rap()
# iu.dance()
# iu.cow()

# Person.class_method()
# Person.static_method(1, 2)

# print(iu)

# iu.cow()

# class Person():
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Person.count += 1

# man = Person('iu').name
# woman = Person('bts')
# print(man)

