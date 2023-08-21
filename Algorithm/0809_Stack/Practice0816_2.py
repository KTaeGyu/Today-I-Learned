string = '(6+5*(2-8)/2)'

stack1 = []
stack2 = []
icp = {'(':3, '*':2. '/':2, '+':1, '-':1}
isp = {'(':0, '*':2. '/':2, '+':1, '-':1}

for i in string:
    if i.isdigit():
        stack1.append(i)
    elif i in '(+-*/)':
        if i 