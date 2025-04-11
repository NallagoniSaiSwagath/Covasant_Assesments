class Poly:
    def __init__(self, *coeffs):
        self.coeffs = list(coeffs)

    def __add__(self, other):
        a = self.coeffs
        b = other.coeffs
        if len(a) < len(b):
            a = [0] * (len(b) - len(a)) + a
        elif len(b) < len(a):
            b = [0] * (len(a) - len(b)) + b

        result_coeffs = [x + y for x, y in zip(a, b)]
        return Poly(*result_coeffs)

    def __repr__(self):
        return f"Poly({','.join(map(str, self.coeffs))})"
a = Poly(1,2,3)  
b = Poly(1,0,1,1,2,3)
c = a+b 
print(c)