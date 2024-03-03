
#PDA
#Dogareci Bianca Alexandra
#Potlog Ioana
#grupa 143

from collections import defaultdict

def load_pda_from_file(filename):
    pda = {
        'states': set(),
        'sigma': set(),
        'gamma': set(),
        'delta': defaultdict(list),
        'start': None,
        'final': set()
    }

    with open(filename, 'r') as file:
        section = None
        for line in file:
            line = line.strip()
            if line.startswith('[') and line.endswith(']'):
                section = line[1:-1]
            elif section == 'States':
                pda['states'].add(line)
            elif section == 'Sigma':
                pda['sigma'].add(line)
            elif section == 'Gamma':
                pda['gamma'].add(line)
            elif section == 'Delta':
                parts = line.split(',')
                state = parts[0]
                symbol = parts[1]
                stack_top = parts[2]
                next_state = parts[3]
                stack_push = parts[4]
                key = (state, symbol, stack_top)
                if key not in pda['delta']:
                    pda['delta'][key] = []
                pda['delta'][key].append((next_state, stack_push))
            elif section == 'Start':
                pda['start'] = line
            elif section == 'Final':
                pda['final'].add(line)

    return pda





def run_pda(pda, input_string,stack,current_state):
    global check
    if not check:
        if input_string!="":
            symbol=input_string[0]
            try:
                stack_top = stack[-1]
                key = (current_state, symbol, stack_top)
                if key in pda['delta'].keys():
                    transitions = pda['delta'][key]
                    next_state = transitions[0][0]
                    stack_push = transitions[0][1]
                    if stack_push =='e':
                        stack.pop()
                    if stack_push != 'e':
                        stack[-1] = stack_push
                    check=run_pda(pda,input_string[1:],stack,next_state)

                key = (current_state, 'e', stack_top)
                if key in pda['delta'].keys():
                    transitions = pda['delta'][key]
                    next_state = transitions[0][0]
                    stack_push = transitions[0][1]
                    if stack_push =='e':
                        stack.pop()
                    if stack_push != 'e':
                        stack[-1] = stack_push
                    check = run_pda(pda,input_string, stack, next_state)
            except:
                pass
            key = (current_state,symbol ,'e')
            if key in pda['delta'].keys():
                transitions = pda['delta'][key]
                next_state = transitions[0][0]
                stack_push = transitions[0][1]
                if stack_push != 'e':
                    stack.append(stack_push)
                check = run_pda(pda, input_string[1:], stack, next_state)

            key = (current_state, 'e', 'e')
            if key in pda['delta'].keys():
                transitions = pda['delta'][key]
                next_state = transitions[0][0]
                stack_push = transitions[0][1]
                if stack_push != 'e':
                    stack.append(stack_push)
                check = run_pda(pda, input_string, stack, next_state)

        if input_string=="":
            key = (current_state, 'e', '$')
            if key in pda['delta'].keys():
                transitions = pda['delta'][key]
                next_state = transitions[0][0]
                stack_push = transitions[0][1]
                if stack_push =='e':
                    stack.pop()
                if stack_push != 'e':
                    stack[-1] = stack_push
                current_state=next_state

            if len(stack)==0 and current_state in pda['final']:
                check=True
    return check




pda = load_pda_from_file('pda.in')
print(pda)
input=input("Introduce input: ")

'''
accepta orice de forma: 0...01...1  cu nr de 0 si 1 egali, pentru fisierul de intrare trimis
'''

stack = []
current_state = pda['start']
check=False
check = run_pda(pda, input,stack,current_state)

if not check:
    print("Rejected")
else:
    print("Accepted")
