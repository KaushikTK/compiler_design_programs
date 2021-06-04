prods = [['E','E*E'],['E','E+E'],['E','(E)'],['E','a']]

ip = '(a+a)'
print('The input string is: '+ str(ip))
stack = ''

ip = list(ip)

for i in range(len(ip)):
    stack += ip[i]
    stacklist = list(stack)
    stacklist = stacklist[::-1]
    temp = ''

    for j in stacklist:
        temp+=j
        if(temp == prods[0][1]):
            stack = stack.replace(prods[0][1], prods[0][0])
            temp = temp.replace(prods[0][1],prods[0][0])

        if(temp == prods[1][1]):
            stack = stack.replace(prods[1][1], prods[1][0])
            temp = temp.replace(prods[1][1],prods[1][0])

        if(temp == prods[2][1]):
            stack = stack.replace(prods[2][1], prods[2][0])
            temp = temp.replace(prods[2][1],prods[2][0])

        if(temp == prods[3][1]):
            stack = stack.replace(prods[3][1], prods[3][0])
            temp = temp.replace(prods[3][1],prods[3][0])
#print((stack))

while len(stack) > 1:
    t = list(stack)
    temp = ''
    for i in t:
        temp += i
        if(temp == prods[0][1]):
            stack = stack.replace(prods[0][1], prods[0][0])
            temp = temp.replace(prods[0][1],prods[0][0])

        if(temp == prods[1][1]):
            stack = stack.replace(prods[1][1], prods[1][0])
            temp = temp.replace(prods[1][1],prods[1][0])

        if(temp == prods[2][1]):
            stack = stack.replace(prods[2][1], prods[2][0])
            temp = temp.replace(prods[2][1],prods[2][0])

        if(temp == prods[3][1]):
            stack = stack.replace(prods[3][1], prods[3][0])
            temp = temp.replace(prods[3][1],prods[3][0])

print('Input after parsing is : ' + str(stack))