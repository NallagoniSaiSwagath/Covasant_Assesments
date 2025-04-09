"""flatten(lst)        Flattens the list 
                    ie input = [1,2,3, [1,2,3,[3,4],2]]
                    output = [1,2,3,1,2,3,3,4,2]
"""
input = [1,2,3, [1,2,3,[3,4],2]]
output=[]
def flatten(lst):
    for l in lst:
        if type(l) != list:
            output.append(l)
        else:
             return flatten(l)
    return output
output=flatten(input)
print(output)
