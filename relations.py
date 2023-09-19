## Classes for the relations between propositions in phrases

class Proposition:
    def __init__(self, value: str, truth: bool = True):
        self.value = value
        self.truth = truth
    
    def __str__(self):
        return str(self.value)
        
    def set_truth(self, truth):
        self.truth = truth
        
    def get_truth(self):
        return self.truth        
    
     

## make it so when proposition value changes the not value changes
class Not:
    def __init__(self, prop: Proposition):
        self.prop = prop
        
    def __str__(self):
        return "~" + str(self.prop.value)
    
    def get_truth(self) -> bool:
        return not self.prop.get_truth()


#prop1 ^ prop2
class And:
    def __init__(self, prop1: Proposition, prop2: Proposition):
        self.prop1 = prop1
        self.prop2 = prop2
        
    def __str__(self):
        return str(self.prop1) + " ^ " + str(self.prop2)
    
    def get_truth(self) -> bool:
        if self.prop1.get_truth() is True and self.prop2.get_truth() is True:
            return True
        return False
    

#prop1 v prop2
class Or:
    def __init__(self, prop1: Proposition, prop2: Proposition):
        self.prop1 = prop1
        self.prop2 = prop2
        
    def __str__(self):
        return str(self.prop1) + " v " + str(self.prop2)
    
    def get_truth(self) -> bool:
        if self.prop1.get_truth() is True or self.prop2.get_truth() is True:
            return True
        return False
    
## format of prop1 -> prop2      
class Conditional:
    def __init__(self, prop1: Proposition, prop2: Proposition):
        self.prop1 = prop1
        self.prop2 = prop2
        
    def __str__(self):
        return str(self.prop1) + " -> " + str(self.prop2)
    
    def get_truth(self) -> bool:
        if self.prop1.get_truth() is True and self.prop2.get_truth() is False:
            return False
        return True

# format of prop1 <--> prop2  
class Biconditional:
    def __init__(self, prop1: Proposition, prop2: Proposition):
        self.prop1 = prop1
        self.prop2 = prop2
        
    def __str__(self):
        return str(self.prop1) + " <--> " + str(self.prop2)
    
    def get_truth(self) -> bool:
        if (self.prop1.get_truth() is True and self.prop2.get_truth() is True) or (self.prop1.get_truth() is False and self.prop2.get_truth() is False):
            return True
        return False