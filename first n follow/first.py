NoOfProds = int(input('Enter the number of productions: '))

dic = {}
prods = {}

for _ in range(NoOfProds):
    prod = input('Enter the production like A->x/y format.. : ')
    [left,right] = prod.split('->')
    right = right.split('/')
    temp = []
    for i in range(len(right)):
        temp.append(right[i])
        if(right[i] == 'eps'): right[i] = 'eps'
        else: right[i] = right[i][0]
    dic[left] = right
    prods[left] = temp

keys = dic.keys()
ans = {}

def check(i):
    if(i == 'eps'): return True
    elif(i.isalpha() and i.isupper()): return False
    else: return True

not_proper = [] 
for key in keys:
    arr = dic[key]
    first = []
    for i in arr:
        if check(i) == True:first.append(i)
        else: 
            first.append(i)
            not_proper.append(key)
    ans[key] = first


if(len(not_proper) != 0):flag = False

while(True):
    new_not_proper = []
    for i in not_proper:
        temp = []
        #print(str(i))
        for j in i:
            #print(str(j))
            k = ans[j]
            for p in k:
                #first = ans[p]
                first = ans.get(p,None)
                if first == None: continue
                print(str(first))
                for m in first: 
                    if check(m) == False and i not in new_not_proper:
                        new_not_proper.append(i)
                        if flag == True: flag = False
                    temp.append(m)
        kau = ans.get(i,None)
        if kau == None:ans[i] = temp
        else:
            roo = []
            for z in kau:
                if z.isupper(): pass
                else: roo.append(z)
            ans[i] = roo+temp

        #print(str(temp))
    not_proper = new_not_proper
    if len(not_proper) == 0:
        break

print(str(ans))

'''
E->TA
A->+TA/eps
T->FB
B->*FB/eps
F->(E)/x
'''

not_found = []

def getFollowFor3(A, alpha, B, beta, follow):
    firstPosOfBeta = ans.get(beta,None)
    if(firstPosOfBeta == None): firstPosOfBeta = [beta]
    if 'eps' not in firstPosOfBeta:
        return firstPosOfBeta
    else:
        tempFollow = []
        for i in firstPosOfBeta:
            if(i == 'eps'): pass
            else: tempFollow.append(i)
        t = follow.get(A,None)
        if(t == None): 
            not_found.append([B,A])
            return []
        else:
            for i in t: tempFollow.append(i)
        return tempFollow

def getFollowFor2(A, alpha, B, follow):
    t = follow.get(A,None)
    if(t == None):
        not_found.append([B,A])
        return []
    else: return t

def getFollowFor3like2(A,alpha,B,follow):
    t = getFollowFor2(A,alpha,B,follow)
    if len(t) == 0: return []
    else: return t

follow = {'B':['$']}

for i in prods.keys():
    productions = prods[i] #array
    for j in productions:
        #if(j == 'eps' or len(j) == 1): pass
        if j == 'eps': pass
        elif len(j)==1 and j!='eps':
            if j.isupper():
                ansFromfunction = getFollowFor2(i,None,j,follow)
                if(len(ansFromfunction) == 0): pass
                else:
                    t = follow.get(B,None)
                    if(t == None):follow[B] = ansFromfunction
                    else:
                        for a in ansFromfunction: t.append(a)
                        follow[B] = t
        else:
            if(len(j) == 2):
                A = i
                alpha = j[0]
                B = j[1]
                ansFromfunction = getFollowFor2(A,alpha,B,follow)
                if(len(ansFromfunction) == 0): pass
                else:
                    t = follow.get(B,None)
                    if(t == None):follow[B] = ansFromfunction
                    else:
                        for a in ansFromfunction: t.append(a)
                        follow[B] = t
            
            else:
                A = i
                alpha = j[0]
                B = j[1]
                beta = j[2]
                ansFromfunction = getFollowFor3(A,alpha,B,beta,follow)
                if len(ansFromfunction) == 0: pass
                else:
                    t = follow.get(B,None)
                    if(t == None):follow[B] = ansFromfunction
                    else:
                        for a in ansFromfunction: t.append(a)
                        follow[B] = t


for i in prods.keys():
    productions = prods[i] #array
    for j in productions:
        if(j == 'eps' or len(j) <= 2): pass
        else:
            A = i
            alpha = j[0]
            B = j[1]
            beta = j[2]

            if(beta.isupper()):
                ansFromfunction = getFollowFor3like2(A,alpha,beta,follow)
                t = follow.get(beta,None)
                if(t == None): follow[beta] = t
                else:
                    #for a in ansFromfunction: t.append(a)
                    temp = ansFromfunction + t
                    t = list(set(temp))
                    follow[beta] = t




print(str(follow))
print(str(not_found))




#follow = {'E':['$']}
#check = {}
#print(str(prods))
##flag = True
##while flag == True:
#for i in prods.keys():
#    productions = prods[i] #array
#    for j in productions:
#        if(j == 'eps'): pass
#        else:
#            if(len(j) == 2):
#                A = i
#                alpha = j[0]
#                B = j[1]
#                alreadyPresentInB = follow.get(B,None)
#                alreadyPresentInA = follow.get(A,None)
#                if(alreadyPresentInB == None):
#                    if(alreadyPresentInA != None):
#                        alreadyPresentInA = set(alreadyPresentInA)
#                        follow[B] = list(alreadyPresentInA)
#                    else: follow[B] = [A]
#                else:
#                    if(alreadyPresentInA != None):
#                        for t in alreadyPresentInA:
#                            alreadyPresentInB.append(t)
#                        alreadyPresentInB = set(alreadyPresentInB)
#                        follow[B] = list(alreadyPresentInB)
#                    else: follow[B] = [A]
                
#            elif(len(j) == 3):
#                A = i
#                alpha = j[0]
#                B = j[1]
#                beta = j[2]

#                firstpos = ans.get(beta,None)
#                if(firstpos == None): firstpos = [beta]
#                alreadyPresentInB = follow.get(B,None)
#                alreadyPresentInA = follow.get(A,None)

#                if('eps' not in firstpos):
#                    if alreadyPresentInB == None:
#                        alreadyPresentInB = firstpos
#                    else:
#                        for fp in firstpos:
#                            alreadyPresentInB.append(fp)
#                    alreadyPresentInB = set(alreadyPresentInB)
#                    follow[B] = list(alreadyPresentInB)
                
#                else:
#                    if alreadyPresentInB == None:
#                        tmp = []
#                        for fp in firstpos:
#                            if(fp != 'eps'): tmp.append(fp)
#                        if alreadyPresentInA != None:
#                            for a in alreadyPresentInA:
#                                tmp.append(a)
#                        else: tmp.append(A)
                        
#                        tmp = set(tmp)
#                        follow[B] = list(tmp)
                    
#                    else:
#                        for fp in firstpos:
#                            if(fp != 'eps'): alreadyPresentInB.append(fp)
#                        if alreadyPresentInA != None:
#                            for a in alreadyPresentInA:
#                                alreadyPresentInB.append(a)
#                        else: alreadyPresentInB.append(A)
#                        alreadyPresentInB = set(alreadyPresentInB)
#                        follow[B] = list(alreadyPresentInB)
##if len(follow.keys()) == 5:
##    flag = False

#print(str(follow))