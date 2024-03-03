
#NFA
#Dogareci Bianca Alexandra
#Potlog Ioana
#grupa 143

def dicti(fisier):
    f = open(fisier, "r")
    linii = f.readlines()
    for i in range(len(linii)):
        linii[i] = linii[i].replace("\n", "")
    d={}
    for linie in linii:
        if linie[0]!="#":
            if linie[0]=="[" and linie[len(linie)-1]=="]":
                if linie in d:
                    return "Eroare!"
                else:
                    d[linie]=[]
                    nume=linie
            else:
                d[nume]=d[nume]+[linie]
    return d


def recognise_keys(dict):
    nume=["[Sigma]","[States]","[Delta]"]
    for n in nume:
        if n not in dict:
            return "Eroare!"


def alph(d):
    alphabet=d["[Sigma]"]    #alfabetul
    return alphabet


def state(d):
    ok=0
    states=d["[States]"]
    final=[]
    initial=[]
    for i in range(len(states)):
        states[i]=states[i].replace(",","")
        j=states[i].split()
        if len(j)>3:
            ok=1
        if len(j)!=1:
            if "F" in j[1:]:
                final=final+[states[i][:2]]
            if "S" in j[1:]:
                initial=initial+[states[i][:2]]
    if len(initial)>1:
        ok=1
    dstates={}
    dstates["S"]=initial
    dstates["F"]=final
    if ok!=1:
        return dstates
    else:
        return "Eroare"


def delta(d):
    paths=d["[Delta]"]
    ok=0
    for i in range(len(paths)):
        paths[i]=paths[i].replace(",","")
    dict={}
    for path in paths:
        path=path.split()
        if len(path)!=3:
            ok=1
        try:
            dict[path[0]]=dict[path[0]]+[[path[1],path[2]]]
        except:
            dict[path[0]]=[[path[1], path[2]]]
    if ok==0:
        return dict
    else:
        return "Eroare!"


global check


#NFA
#Dogareci Bianca Alexandra
#Potlog Ioana
#grupa 143

def emulated_nfa(alphabet, states, paths, q,check, s1):
    if check==0:
        if s1!="":
            try:
                for path in paths[q]:
                    if path[0]==s1[0]:
                        q=path[1]
                        s2=s1[1:]
                        check= emulated_nfa(alphabet, states, paths, q, check, s2)
                    if path[0]=="E":
                        q = path[1]
                        check= emulated_nfa(alphabet, states, paths, q, check, s1)
            except:
                pass
        else:
            try:
                for path in paths[q]:
                    if path[0]=="E":
                        q = path[1]
                        check= emulated_nfa(alphabet, states, paths, q, check, s1)
            except:
                for final_state in states["F"]:
                    if final_state==q:
                        check=1
    return check

    # main   -   verificarea erorilor si organizarea datelor prin apelarea functiilor pentru nfa

check = dicti("nfa.in")
if check == "Eroare!":
    print(check)
else:
    d = check
    check = recognise_keys(d)
    if check == "Eroare!":
        print(check)
    else:
        alphabet = alph(d)
        states = state(d)
        if states == "Eroare!":
            print(states)
        else:
            paths = delta(d)
            print(d)
            print(alphabet)
            print(states)
            print(paths)
            s1=input("Introduce input: ")
            c = 0
            for s in s1:
                if s not in alphabet:
                    c = 1
            if c == 0:
                q = states['S'][0]   #starea initiala
                check=0   #adica presupunem ca nu e bun
                check=emulated_nfa(alphabet, states, paths, q, check, s1)
                if check==1:
                    print("DA")
                else:
                    print("NU")
            else:
                print("Nu se poate verifica sirul deoarece contine elemente care nu sunt in alfabet!")


