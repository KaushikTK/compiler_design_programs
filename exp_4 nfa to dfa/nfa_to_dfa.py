from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

states = input('Enter states separated by ",": ')
states = states.split(',')
states = set(states)

symbols = input('Enter symbols separated by ",": ')
symbols = symbols.split(',')
symbols = set(symbols)

transitions = {}

print('Enter the transitions')

while True:
    start = input('Enter the starting state: ')
    on = input('Enter the symbol for transition: ')
    
    t = {}

    data = transitions.get(start,'')
    if(data):
        print(str(data))
        t = data.copy()

    li = input('Enter transition states separated by "," without any space : ')

    li = li.split(',')
    li = set(li)
    t[on] = li
    transitions[start] = t

    x = input('To continue entering more transitions, please enter "y" ')
    if(x != 'y'):
        break

initialState = input('Enter initial state: ')

finalState = input('Enter the final states separated by "," : ')
finalState = finalState.split(',')
finalState = set(finalState)

for i in finalState:
    if(transitions.get(i,None) == None):
        transitions[i] = {"":{}}

print(str(symbols))
print(str(states))
print(str(transitions))
print(str(initialState))
print(str(finalState))

nfa = NFA(
    states=states,
    input_symbols=symbols,
    transitions=transitions,
    initial_state=initialState,
    final_states=finalState
)
#nfa = NFA(
#    states={'q0','q1','q2','q3','q4'},
#    input_symbols={'0','1'},
#    transitions={
#        'q0': {'': {'q2', 'q1'}}, 'q1': {'0': {'q3'}}, 'q2': {'1': {'q3'}}, 'q3': {'1': {'q4'}}, 'q4':{'':{}}
#    },
#    initial_state='q0',
#    final_states={'q4'}
#)

    #states={'q0', 'q1', 'q2'},
    #input_symbols={'a', 'b'},
    #transitions={
    #    'q0': {'a': {'q1'}},
    #    # Use '' as the key name for empty string (lambda/epsilon) transitions
    #    'q1': {'a': {'q1'}, '': {'q2'}},
    #    'q2': {'b': {'q0'}}
    #},
    #initial_state='q0',
    #final_states={'q1'}


dfa = DFA.from_nfa(nfa)

print()
print(dfa.final_states)
print()
print(dfa.transitions)
print()




