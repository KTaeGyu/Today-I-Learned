## Practice

greeting = "hello world"

print(greeting[6])
print(greeting[:5])
print(greeting[6:])
print(greeting[::-1])
print(len(greeting))
for i in range(len(greeting)):
    print(greeting[i], end="")
print()
print(''.join(greeting[i] for i in range(len(greeting))), end="")
print()