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
    
    ps = sorted(list(props), key=lambda x: x.value)
    for i in range(rows):
        vals = bin(i)[2:]
        vals = vals[0:columns] if len(vals) >= columns else "0"*(columns-len(vals)) + vals
        values = [bool(int(i)) for i in vals]
        
        for j in range(columns):
            ps[j].set_truth(values[j])
            
        if with_props: #if props are wanted in the table add them
            for hyp in hypothesis:
                values.append(hyp.get_truth())
        
        values.append(phrase.get_truth())
        
        table.append(values)
    table.append([])
    if with_props:
        table[-1] += ps
    for hyp in hypothesis:
        table[-1].append(hyp)        
    table[-1].append(phrase)
    table.reverse()
    return table   


def make_props_table(props: set, hypothesis, conclusion):   
    table = generate_table_with_hyp(props, hypothesis, conclusion ,with_props=False)
    return table
def test():
    #hypothesis
    p1 = "q v p ->"
    p2 = "p"
    
    props1, conc1 = gen_props_and_phrase(p1)
    props2, conc2 = gen_props_and_phrase(p2)
    props1.union(props2)
    print(*props1)
    #conclusion
    c = "p"
    props3, conclusion = gen_props_and_phrase(c)
    props1.union(props3)
    
    table = make_props_table(props1, [conc1, conc2], conclusion)
    print(display_table(table))
    print(is_valid(table))
    


test()
    
        
            