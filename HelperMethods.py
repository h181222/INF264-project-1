from math import log2

class HelperMethods(object):
    
    #method to count how many occurences a value in a set(i.e attributes)
    def value_count(y):
        result = {}
        for value in y:
            if value not in result:
                result[value] = 1
            else:
                result[value]+=1
        return result
    
    
    def entropy(y):
        result = value_count(y)
        entropy = 0
        for value in result.values():
            p = value/len(y)
            entropy -= p*log2(p)
        return entropy
    

    
    
    
    
    
    
    