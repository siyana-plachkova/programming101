class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        if self.numerator == 0:
            return "0"

        if self.denominator == 1:
            return "{}".format(self.numerator)

        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        new_self = self.simplify()
        new_other = other.simplify()

        eq_numerator = new_self.numerator == new_other.numerator
        eq_denominator = new_self.denominator == new_other.denominator

        return eq_numerator and eq_denominator

    def __add__(self, other):
        first_numerator = self.numerator * other.denominator
        second_numerator = other.numerator * self.denominator
        new_numerator = first_numerator + second_numerator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator).simplify()

    def __sub__(self, other):
        first_numerator = self.numerator * other.denominator
        second_numerator = other.numerator * self.denominator
        new_numerator = first_numerator - second_numerator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator).simplify()

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator).simplify()

    def simplify(self):
        new_numerator = self.numerator
        new_denominator = self.denominator

        for i in range(min(new_numerator, new_denominator), 1, -1):
            if new_denominator % i == 0 and new_numerator % i == 0:
                new_numerator /= i
                new_denominator /= i

        return Fraction(new_numerator, new_denominator)

if __name__ == '__main__':
    a = Fraction(1, 2)
    b = Fraction(2, 4)

    print(a == b)
    print(a + b)
    print(a - b)
    print(a * b)
