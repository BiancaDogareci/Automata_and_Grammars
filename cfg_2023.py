
#CFG
#Dogareci Bianca Alexandra
#Potlog Ioana
#grupa 143

def dicti(fisier):
    f=open(fisier,"r")
    linii=f.readlines()
    for i in range(len(linii)):
        linii[i]=linii[i].replace("\n","")
        linii[i] = linii[i].replace(" ", "")
    d={}
    for linie in linii:
        if linie[0]=="[":
            d[linie]=[]
            key=linie
        else:
            d[key]=d[key]+[linie]
    return d

def variables(d):
    var = d["[Var]"]
    if 'S' not in var:
        return "Error!"
    else:
        return var

def rules(d):
    rules={}
    r=d["[Rules]"]
    for rule in r:
        s=rule.split("-")
        s[1]=s[1].split(";")
        rules[s[0]]=s[1]
    return rules

import random
def cfg_recursion(var,final,rules):
    s='S'
    s=random.choice(rules['S'])
    s=s.split(",")
    ok=1
    while ok==1:
        count=0
        new=s
        index=-1
        for i in range(len(s)):
            if s[i] in var:
                ls=random.choice(rules[s[i]]).split(",")
                if index==-1:
                    index=i
                new=new[:index]+ls+new[index+1:]
                index=index+len(ls)
                count=1
            else:
                if index!=-1:
                    index=index+1
        s=new
        if count==0:
            ok=0
    return s



d=dicti("cfg.in")
var=variables(d)
if var=="Error!":
    print(var)
else:
    final = d["[Sigma]"]
    rules=rules(d)
    '''
    print(d)
    print(var)
    print(final)
    print(rules)
    '''
    random=cfg_recursion(var,final,rules)
    print(random)



