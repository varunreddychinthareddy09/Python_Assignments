class Poly:
    def __init__(self, *coefficients):
        self.coefficients = list(coefficients)
    
    def __str__(self):
        return "Poly(" + ", ".join(map(str, self.coefficients)) + ")"

    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coefficients = [0] * max_len

        for i in range(1, len(self.coefficients) + 1):
            new_coefficients[-i] += self.coefficients[-i] 

        for i in range(1, len(other.coefficients) + 1):
            new_coefficients[-i] += other.coefficients[-i]

        return Poly(*new_coefficients)
