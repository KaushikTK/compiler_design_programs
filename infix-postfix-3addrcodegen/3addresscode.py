OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRI = {'+':1, '-':1, '*':2, '/':2}

def convert(formula):
    stack = [] # only pop when the coming op has priority 
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop() # pop '('
        else:
            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    # leftover
    while stack: 
    	output += stack.pop()
    return output

ans = []


def generate3AC(pos):
	exp_stack = []
	t = 1; global ans
	
	for i in pos:
		if i not in OPERATORS:
			exp_stack.append(i)
		else:
			ans.append(['t'+str(t), str(exp_stack[-2]), str(i), str(exp_stack[-1])])
			exp_stack=exp_stack[:-2]
			exp_stack.append(f't{t}')
			t+=1

expres = input("Enter the expression: ")
print()
pos = convert(expres)
generate3AC(pos)


print('Quadruple Representation:')
for i in range(0,len(ans),1):
    operand1 = ans[i][1]
    operand2 = ans[i][3]
    op = ans[i][2]
    temp = ans[i][0]
    
    print(op + ' ' + operand1 + ' ' + operand2 + ' ' + temp)
print()
    
print('Triple Representation:')
for i in range(0,len(ans),1):
    operand1 = ans[i][1]
    operand2 = ans[i][3]
    op = ans[i][2]

    if 't' in operand1: operand1 = '(' + operand1[1] + ')'
    if 't' in operand2: operand2 = '(' + operand2[1] + ')'
    
    print(op + ' ' + operand1 + ' ' + operand2)
print()

print('Indirect Triple Representation:')
for i in range(0,len(ans),1):
    operand1 = ans[i][1]
    operand2 = ans[i][3]
    op = ans[i][2]

    if 't' in operand1: operand1 = '(' + operand1[1] + ')'
    if 't' in operand2: operand2 = '(' + operand2[1] + ')'
    
    print(op + ' ' + operand1 + ' ' + operand2)
print()

