# print(help(list))
'''class list(object)
 |  list(iterable=(), /)
 |
 |  Built-in mutable sequence.
 |
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |
 |  Methods defined here:'''

# print(help(dict))
'''class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |
 |  Methods defined here:'''
# string1 = 'HELLO'
# print(string1.isupper()) # True
# print(string1.islower()) # False
# print(string1.isalpha()) # True
# print(string1.istitle()) # True

# text = 'Hello, world!'

# # s.replace(old, new[,count])
# new_text = text.replace('world', 'Python')
# print(new_text) # Hello, Python!

# # s.strip([chars])
# new_text = text.strip('d')
# print(new_text) # Hello, world!


# lst1 = [1, 2, [3, 4]]
# lst2 = list(lst1)

# lst2[2][0] = 100
# print(lst1, lst2) # [1, 2, 3] [100, 2, 3]


# # set 실습
# l1 = [1, 2, 3]
# l2 = [4, 5, 6, 7, 8, 9]
# s1 = set(l1)
# s2 = set(l2)

# s1.add(4)
# print(s1)

# s1.update([5, 6, 7])
# print(s1)

# s1.remove(7)
# s1.discard(7)
# print(s1)

# a2 = s1 - s2
# a = s1.difference(s2)
# print(a, a2)

# b2 = s1 & s2
# b = s1.intersection(s2)
# print(b, b2)

# c2 = s1 | s2
# c = s1.union(s2)
# print(c, c2)



# # 딕셔너리 실습
# from pprint import pprint

# eng = {
#     'plus' : ['더하기', '장점'], 
#     'minus': ['빼기', '적자'], 
#     'multiply': ['곱하기', '다양하게'], 
#     'division': ['나누기', '분열']
#     }

# def eng_meaning1(dict, key):
#     value = dict[key]
#     print(f'{key}의 뜻: {value}')


# def eng_meaning2(dict, key):
#     value = dict.get(key, '등록되어 있지 않음')
#     print(f'{key}의 뜻: {value}')

# eng_meaning1(eng, 'plus')
# eng_meaning2(eng, 'plus')


# def eng_list(dict):
#     words = []
#     for key in dict.keys():
#         words.append(key)
#     print(f'등록된 단어: {words}')

# eng_list(eng)


# def eng_add(dict, new_let, *meaning):
#     dict[new_let] = list(meaning)
#     print(
#         f'새로운 단어 {new_let} 이/가 추가되었습니다.\n\
#         뜻은 {list(meaning)} 입니다.'
#         )

# eng_add(eng, 'square', '제곱', '사각형')
# pprint(eng)


# def eng_pop(dict, word):
#     if word in dict.keys():
#         eng.pop(word)
#         print(f'이 사전에서 {word} 단어를 제거하였습니다.')
#     else:
#         print(f'이 사전에는 {word} 단어가 존재하지 않습니다.')

# eng_pop(eng, 'plus')


# def eng_del(dict, word):
#     try:
#         del dict[word]
#         print(f'이 사전에서 {word} 단어를 제거하였습니다.')
#     except:
#         print(f'이 사전에는 {word} 단어가 존재하지 않습니다.')

# eng_del(eng, 'plus')


# # 카운팅 실습
# # 방법 1 카운터 함수 호출
# from collections import Counter
# blood_types = ['A', 'B', 'A', 'O', 'AB', 'A']
# result = dict(Counter(blood_types))
# print(result)

# # 방법 2 조건문
# new_dict1 = {}
# for blood_type in blood_types:
#     if blood_type in new_dict1:
#         new_dict1[blood_type] += 1
#     else:
#         new_dict1[blood_type] = 1
# print(new_dict1)

# # 방법 3 .get(k[,default])
# new_dict2 = {}
# for blood_type in blood_types:
#     new_dict2[blood_type] = new_dict2.get(blood_type, 0) + 1
# print(new_dict2)

# # 방법 4 .stedefault(blood_type[,default])
# new_dict3 = {}
# for blood_type in blood_types:
#     new_dict3.setdefault(blood_type, 0)
#     new_dict3[blood_type] += 1
# print(new_dict3)


# # 해시 함수 실습
# s1 = {1, 2, 3, 54, 73, 515, 5367, 123, 's', 'o'}

# # for i in s1:
# #     print(hash(i))

# for x in range(len(s1)):
#     a = s1.pop()
#     print(hash(a))