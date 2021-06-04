productions = ["E=E+T",
     "T=T*F",
     "F=(E)",
     "F=i"]

rules = {}
terms = []
for i in productions:
    temp = i.split("=")
    terms.append(temp[0])
    try: rules[temp[0]] += [temp[1]]
    except: rules[temp[0]] = [temp[1]]

terms = list(set(terms))
#print(rules,terms)

def check_if_operator_grammar(prod):
    if str(prod) == 'eps': return False
    if len(prod) == 1: return True
    else:
        n = len(prod)
        for i in range(0,n-1,1):
            if(str(prod[i]).isalpha() and str(prod[i+1]).isalpha() == True):
                if str(prod[i]).isupper() and str(prod[i+1]).isupper() == True: return False
        return True


flag = True
for i in terms:
    prods = rules[i]
    for j in prods:
        if check_if_operator_grammar(j) == False:
            print("The given grammar is not an operator grammar")
            flag = False
            break

def leading(gram, rules, term, start):
    s = []
    if gram[0] not in terms:
        return gram[0]
    elif len(gram) == 1:
        return [0]
    elif gram[1] not in terms and gram[-1] is not start:
        for i in rules[gram[-1]]:
            s+= leading(i, rules, gram[-1], start)
            s+= [gram[1]]
        return s


def trailing(gram, rules, term, start):
    s = []
    if gram[-1] not in terms:
        return gram[-1]
    elif len(gram) == 1:
        return [0]
    elif gram[-2] not in terms and gram[-1] is not start:

        for i in rules[gram[-1]]:
            s+= trailing(i, rules, gram[-1], start)
            s+= [gram[-2]]
        return s

if flag == True:
    leads = {}
    trails = {}
    for i in terms:
        s = [0]
        for j in rules[i]:
            lead_tmp = leading(j,rules,i,i)
            #s+=leading(j,rules,i,i)
            s+=lead_tmp
        s = set(s)
        s.remove(0)
        leads[i] = s
        s = [0]
        for j in rules[i]:
            trail_temp = trailing(j,rules,i,i)
            #s+=trailing(j,rules,i,i)
            s+=trail_temp
        s = set(s)
        s.remove(0)
        trails[i] = s


    for i in terms:
        print("leading("+i+"):",leads[i])
    for i in terms:
        print("trailing("+i+"):",trails[i])