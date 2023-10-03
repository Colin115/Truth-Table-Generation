from relations import *
def identify_props(phrase, props) -> set:
    letters = 'abcdefghijlkmnopqrstuwxyz'
    for letter in phrase:
        if letter in letters and not any(letter == p.value for p in props):
            props.add(Proposition(letter))
    return props
            

def find_nots(phrase) -> list:
    i = 0
    while i < len(phrase):
        value = phrase[i]
        if value == "~":
            phrase = phrase[:i] + [Not(phrase[i+1])] + phrase[i+2:] if (i < len(phrase)-1) else phrase[:i] + [Not(phrase[i+1])]
            i -= 1
        i += 1
    return phrase

def make_compound_props(phrase) -> str:
    arg1, arg2 = phrase[0], phrase[-1]
    sign = "".join(phrase[1:len(phrase)-1])
    
    if sign == "^": # and 
        return And(arg1, arg2)
    elif sign == "v": # or
        return Or(arg1, arg2)
    elif sign == "->":
        return Conditional(arg1, arg2)
    elif sign == "<->":
        return Biconditional(arg1, arg2)
    else:
        raise ValueError(f"Invalid symbol found: {sign}")
        
    

def indentify_groups(phrase) -> str:
    # return if there are no special groupings
    
    conditions = ["("]
    while any(condition in phrase for condition in conditions):
        inner = None
        
        i = 0
        while i < len(phrase):
            letter = phrase[i]
            if letter == "(":
                inner = i
            if letter == ")":
                condition = phrase[inner+1:i]
                print(*condition)
                print(*phrase)
                phrase = phrase[:inner] + [make_compound_props(condition)] + phrase[i+1:]
            i += 1
    
    conditions = ['^', "v"]
    while any(condition in phrase for condition in conditions):
        i = 0
        while i < len(phrase):
            letter = phrase[i]
            if letter in ("v", "^"):
                condition = phrase[i-1:i+2]
                phrase = phrase[:i-1] + [make_compound_props(condition)] + phrase[i+2:]
                i -= 1
            i += 1
                
    #make sure conditions are only -> and <->
    while "-" in phrase:
        
        i = 0
        while i < len(phrase):
            letter = phrase[i]
            if letter == "-": #conditional a - > b
                condition = phrase[i-1:i+3]
                
                phrase = phrase[:i-1] + [make_compound_props(condition)] + phrase[i+3:]
                i -= 2
                
            elif letter == "<": #bicondition
                condition = phrase[i-1:i+4]
                phrase = phrase[:i-1] + [make_compound_props(condition)] + phrase[i+4:] 
                i -= 3
            i += 1
            
    return phrase
                
                
def generate_table(props, phrase) -> list[list[bool]]:
    rows = 2**len(props)
    columns = len(props)
    table = []
    
    ps = sorted(list(props), key=lambda x: x.value)
    
    for i in range(rows):
        vals = bin(i)[2:]
        vals = vals[0:columns] if len(vals) >= columns else "0"*(columns-len(vals)) + vals
        values = [bool(int(i)) for i in vals]
        
        for j in range(columns):
            ps[j].set_truth(values[j])
            
        
        values.append(phrase.get_truth())
        
        table.append(values)
    
    table.append(ps)        
    table[-1].append(phrase)
    table.reverse()
    return table   

 
      
def display_table(table):
    header_row = table[0]
    
    #header = " | ".join([str(i) if not i else ("  " + str(i)) for i in header_row])
    
    header = ""
    for i in header_row:
        header += f' {str(i):8} | '
    header = header[0:len(header)-2]
    
    
    table = [header] + [" | ".join([f'  {str(c):7}' for c in row]) for row in table[1:]]
    
    return "\n".join(table)  
    
    

# returns the set of props and the proposition
def gen_props_and_phrase(x="pvq", previous_props=set()) -> tuple:
  
    
    props = identify_props(x, previous_props) # identify each proposition in the phrase
    
    # reformat the phrase into a list
    phrase = [i for i in x]
    phrase = list(filter(lambda x: x!=" ", phrase))
    
    # replace the charectors for their propositions
    for p in props:
        if p.value in phrase:
            phrase = [p if i==p.value else i for i in phrase]
    
    #replace the nots
    phrase = find_nots(phrase)

    #solve groupings
    phrase = indentify_groups(phrase)
    
    final_prop = phrase[0]
    
    return (props, final_prop)
    
    
def main():
    props, final_prop = gen_props_and_phrase(x="p->q")
    table = generate_table(props, final_prop)
    print(display_table(table))
        
            
if __name__ == "__main__":
    main()