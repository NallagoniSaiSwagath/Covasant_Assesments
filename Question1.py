#flatten(lst)        Flattens the list 
 #                   ie input = [1,2,3, [1,2,3,[3,4],2]]
  #                  output = [1,2,3,1,2,3,3,4,2]
cd=[]
def flatten(lst):
    for l in lst:
        if type(l)!= list:
            cd.append(l)
        else:
            flatten(l)
flatten([1,2,3, [1,2,3,[3,4],2]])
print(cd)