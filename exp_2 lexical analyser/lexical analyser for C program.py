import re

f = open('input(C program).txt','r')

operators = { '=': 'Assignment Operator','+': 'Additon Operator', '-' : 'Substraction Operator', '/' : 'Division Operator', '*': 'Multiplication Operator', '++' : 'increment Operator', '--' : 'Decrement Operator'}
optr_keys = operators.keys()

comments = {r'//' : 'Single Line Comment',r'/*' : 'Multiline Comment Start', r'*/' : 'Multiline Comment End', '/**/' : 'Empty Multiline comment'}
comment_keys = comments.keys()

header = {'.h': 'header file'}
header_keys = header.keys()

sp_header_files = {'<stdio.h>':'Standard Input Output Header','<string.h>':'String Manipulation Library'}

datatype = {'int': 'Integer','float' : 'Floating Point', 'char': 'Character','long': 'long int'}
datatype_keys = datatype.keys()

keyword = {'return' : 'keyword that returns a value from a block'}
keyword_keys = keyword.keys()

delimiter = {';':'terminator symbol semicolon (;)'}
delimiter_keys = delimiter.keys()

blocks = {'{' : 'Blocked Statement Body Open', '}':'Blocked Statement Body Closed'}
block_keys = blocks.keys()

builtin_functions = {'printf':'printf prints its argument on the console'}

non_identifiers = ['_','-','+','/','*','`','~','!','@','#','$','%','^','&','*','(',')','=','|','"',':',';','{'
,'}','[',']','<','>','?','/']

funs = ['for','while','do','printf','scanf']

# Flags
dataFlag = False


i = f.read()

count = 0
program =  i.split('\n')

for line in program:
    count = count+1
    print('Line #'+str(count))
    print('Code: '+line)
    seen = []
    #print "Line #",count,"\n",line
    
     
    tokens = line.split(' ')
    #print ("Tokens are"+str(tokens))
    #print('Line #'+str(count))
    print('Information retrieved:')

    #print "Line #",count,'properties \n'
    for token in tokens:
        
        if '\r' in token:
            position = token.find('\r')
            token=token[:position]
        # print 1
        
        if token in block_keys:
            print (str(blocks[token]))
        elif token in optr_keys:
            print (str("Operator is: " + str(operators[token])))
        elif token in comment_keys:
            print (str("Comment Type: " + str(comments[token])))
        elif '.h' in token:
            print( "Header File is: " + ' '+ str(token) + ' ' + str(sp_header_files[token]))

        elif token in datatype_keys:
            print ("type is: "+ str(datatype[token]))
            dataFlag = True
            seen.append(token)
        
        elif token in keyword_keys:
            print (str(keyword[token]))
            
        elif token in delimiter:
            print( "Delimiter"+str(delimiter[token]))
        elif '#' in token:
            match = re.search(r'#\w+', token)
            print ("Header"+ str(match.group()))
        else:
            try:
                if(len(token)>1 and ';' in token):
                    token = token.replace(';','')
                value = float(token)
                print('Constant:'+str(token))
                dataFlag = False
            except ValueError:
                for fun in funs:
                    if fun in token:
                        print ("Print or scan or loops: " + str(fun))
                        break
        
        if dataFlag == True and (token not in non_identifiers) and ('()' not in token) and (token not in seen):
            if(token[0] != ''):
                #val = ord(token[0])
                #if(val >= 'a' )
                if(token[0].isalpha() and '.' not in token):
                    print ("Identifier: "+str(token))

    dataFlag = False
    print ("====================================================")
f.close()