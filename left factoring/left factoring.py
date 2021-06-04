n = int(input('Enter the number of productions: '))
char = ord('A')

for _ in range(n):

    production =  input('Enter the production:')

    [left, right] = production.split('->')
    right = right.split('/')

    counter = 0
    similar = ''
    flag = True

    while flag:
        if(len(right[0]) == counter):
            flag = False
            break
        
        ele = right[0][counter]
        for i in range(1,len(right),1):
            if(counter == len(right[i]) or counter > len(right[i])):
                flag = False
                break
            var = right[i][counter]
            if(var == ele):
                if(i == len(right)-1):
                    similar += ele
                    counter += 1

            else:
                flag = False
                break

    not_similar = [] 

    for i in range(0,len(right),1):
        prod = right[i]
        extra = prod[counter:]
        right[i] = prod[0:counter]
        right[i] += "A'"
        not_similar.append(extra)

    print(left+'->',end='')
    for i in range(len(right)):
        if(i != len(right)-1):
            if(right[i] == ''): print('epsilon/',end='')
            else: print(str(right[i])+'/',end='')
        else:
            if(right[i] == ''): print('epsilon',end='')
            else: print(str(right[i]),end='')

    print()

    print(chr(char)+"' ->",end='')
    char += 1
    for i in range(len(not_similar)):
        if(i != len(not_similar)-1):
            if(not_similar[i] == ''): print('epsilon/',end='')
            else: print(str(not_similar[i])+'/',end='')
        else:
            if(not_similar[i] == ''): print('epsilon',end='')
            else: print(str(not_similar[i]),end='')
    print()