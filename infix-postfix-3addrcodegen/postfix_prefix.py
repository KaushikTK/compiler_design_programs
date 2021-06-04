OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRI = {'+':1, '-':1, '*':2, '/':2}

def convert(formula,type):
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
        
    if(type == 'pre'):
        output = output[::-1]
        print('prefix: ',end='')
    else:
        print('postfix: ',end='')

    print(str(output))
    return output


# for prefix => just reverse the string and change ( to ) and ) to ( and perform infix to postfix
expres = input("INPUT THE EXPRESSION: ")
convert(expres[::-1],'pre')
convert(expres,'post')