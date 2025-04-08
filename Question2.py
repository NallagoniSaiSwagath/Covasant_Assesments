"""
convert(x)          Converts like below 
                    input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
                    output = [[[[0,1,2],[3,4,5]],[[5,6,7],[9,4,2]]]]
"""
input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
def convert(x):
    if isinstance(x, str):
        return list(map(int, x[1:-1].split(',')))
    else:
        return [convert(i) for i in x]
con=convert(input)
print(con)