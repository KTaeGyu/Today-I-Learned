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

text = 'Hello, world!'

# s.replace(old, new[,count])
new_text = text.replace('world', 'Python')
print(new_text) # Hello, Python!

# s.strip([chars])
new_text = text.strip('d')
print(new_text) # Hello, world!