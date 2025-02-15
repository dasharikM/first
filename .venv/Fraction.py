class Fraction:
    def __init__(self, main_part, num, den):
        divider = self.gcd(num, den)
        num //= divider
        den //= divider

        if main_part < 0:
            num = main_part * den - num
        else:
            num = num + main_part * den

        divider = self.gcd(num, den)
        num //= divider
        den //= divider

        if den < 0:
            num *= -1
            den *= -1

        self.numerator = num
        self.denominator = den

    def get_numerator(self):
        return self.numerator

    def set_numerator(self, numerator):
        self.numerator = numerator

    def get_denominator(self):
        return self.denominator

    def set_denominator(self, denominator):
        self.denominator = denominator

    @staticmethod
    def multiply_fractions(num1, den1, num2, den2):
        # Сокращаем крест-накрест
        nod1 = Fraction.gcd(num1, den2)
        num1 //= nod1
        den2 //= nod1

        nod2 = Fraction.gcd(num2, den1)
        num2 //= nod2
        den1 //= nod2

        # Работаем с минусами в дроби
        return Fraction.magic_with_minus(num1 * num2, den1 * den2)

    @staticmethod
    def magic_with_minus(num, den):
        # "a/-b" --> "-a/b"
        # "-a/-b" --> "a/b"
        if den < 0:
            num *= -1
            den *= -1
        return Fraction(0, num, den)

    @staticmethod
    def dividing_fractions(num1, den1, num2, den2):
        return Fraction.multiply_fractions(num1, den1, den2, num2)

    @staticmethod
    def subtracting_fractions(num1, den1, num2, den2):
        nok = Fraction.lcm(den1, den2)
        new_num = num1 * nok // den1 - num2 * nok // den2
        nod = Fraction.gcd(nok, new_num)
        return Fraction.magic_with_minus(new_num // nod, nok // nod)

    @staticmethod
    def adding_fractions(num1, den1, num2, den2):
        return Fraction.subtracting_fractions(num1, den1, -num2, den2)

    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        return Fraction.gcd(b, a % b)

    @staticmethod
    def lcm(a, b):
        return abs(a * b) // Fraction.gcd(a, b)

    def __str__(self):
        if self.denominator == 1:
            return f"{self.numerator} "
        else:
            return f"{self.numerator}/{self.denominator} "