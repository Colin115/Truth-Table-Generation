## Determine if an argument is valid
from props import *

def is_valid(table: list[list[bool]]):
    table = table[1:] #remove header
    rows = len(table)
    columns = len(table[0])
    
    for row in table:
        if all(row[:columns-1]) and not row[-1]:
            return False
    return True


def generate_table_with_hyp(props, hypothesis, phrase, with_props=True) -> list[list[bool]]:
    rows = 2**(len(props))
    columns = len(props)
    table = []
    
    ps = sorted(list(props), key=lambda x: x.value) #sort  individual props alphabetically
    for i in range(rows): #for each truth table possibility
        vals = bin(i)[2:] #make it a binary number to set truth values
        vals = vals[0:columns] if len(vals) >= columns else "0"*(columns-len(vals)) + vals # make sure the binary number is the length of the props
        values = [bool(int(i)) for i in vals] #turn the individual digits of each binary digit into bool values
        
        #set the truth values for each individual prop
        for j in range(columns):
            ps[j].set_truth(values[j])
            
        for hyp in hypothesis: # add the hypothesis into the table
            values.append(hyp.get_truth())
        
        values.append(phrase.get_truth()) #add the conclusion to the table
        
        
        if with_props: #if props are wanted in the table add them
            table.append(values) 
        else:
            table.append(values[len(hypothesis):]) #only add the hypothesis's
     
    #make the header row       
    table.append([])
    if with_props:
        table[-1] += ps
    for hyp in hypothesis:
        table[-1].append(hyp)        
    table[-1].append(phrase)
    table.reverse()
    return table   


def make_props_table(props: set, hypothesis, conclusion):   
    table = generate_table_with_hyp(props, hypothesis, conclusion, with_props=False)
    return table

    
def makeArgument(hypothesis: list[str], conclusion: str):
    props = set() # holds all the letters like p, q, r, t
    formated_hypothesis = [] # holds the hypothesis like p->q
    
    # generate the hypothesis
    for hyp in hypothesis:
        ps, hs = gen_props_and_phrase(hyp)
        props |= ps
        formated_hypothesis.append(hs)
    #make conclusions
    ps, formated_conclusion = gen_props_and_phrase(conclusion)
    props.union(ps)
    #generate table
    table = make_props_table(props, formated_hypothesis, formated_conclusion)
    return table
    
