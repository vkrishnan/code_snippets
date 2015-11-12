def gcd(m,n):
    while m%n != 0:
        m, n = n, m % n
    return n

class Fraction(object):
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, obj):
        num = self.num * obj.den + self.den * obj.num
        den = self.den * obj.den
        common = gcd(num, den)
        return Fraction(num//common, den//common)
        
    def __eq__(self, obj):
        return self.num * obj.den == self.den * obj.num
        
    def __mul__(self, obj):
        num = self.num * obj.num
        den = self.den * obj.den
        common = gcd(num, den)
        return Fraction(num // common, den // common)
        
    def __div__(self, obj):
        num = self.num * obj.den
        den = self.den * obj.num
        common = gcd(num, den)
        return Fraction(num // common, den // common)
        
    def __sub__(self, obj):
        pass
        
    def __lt__(self, obj):
        pass
        
    def __gt__(self, obj):
        pass

f1 = Fraction(1, 2)
f2 = Fraction(1, 2)
print f1
print f2

print f1 * f2
print f1 / f2