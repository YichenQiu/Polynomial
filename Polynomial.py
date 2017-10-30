class Polynomial(object):
    '''Class which behaves like a mathemetical polynomial
    '''
    def __init__(self, coef_list):
        self.coefs = coef_list
        self.degree = len(coef_list) - 1

    def __repr__(self):
        return "'Polynomial({})'".format(self.coefs)

    def __add__(self, other):
        max_degree = max(len(self.coefs), len(other.coefs))

        normed_self = self._normalize_coefs(degree=max_degree)
        normed_other = other._normalize_coefs(degree=max_degree)

        new_coefs = [
            sum(pair)
            for pair in zip(normed_self, normed_other)
        ]

        return Polynomial(new_coefs)

    def __mul__(self, other):
        new_degree = self.degree + other.degree
        new_coefs = [0 for _ in range(new_degree + 1)]

        for power, coef in enumerate(self.coefs):
            for other_power, other_coef in enumerate(other.coefs):
                new_coefs[power + other_power] += coef*other_coef

        return Polynomial(new_coefs)

    def __str__(self):
        str_list = [
            '{coef}x^{power}'.format(coef=coef, power=i)
            for i, coef in enumerate(self.coefs)
            if coef != 0
        ]

        return ' + '.join(str_list[::-1])


    def _normalize_coefs(self, degree=None):
        if degree is None:
            degree = self.degree
        normed_coefs = [0 for i in range(degree)]
        for i, coef in enumerate(self.coefs):
            normed_coefs[i] = coef
        return normed_coefs

    def eval(self, x):
        powers = [
            x**power
            for power, _ in enumerate(self.coefs)
        ]

        return sum([
            coef*power
            for coef, power in zip(self.coefs, powers)
        ])
