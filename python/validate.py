import random
from lagrange import lagrange_interpolate_zero

FIELD = 208351617316091241234326746312124448251235562226470491514186331217050270460481
SECRET = 123456789
THRESHOLD = 3
SHARES = 5
SEED = 1337

random.seed(SEED)

coeffs = [SECRET] + [random.randrange(1, FIELD) for _ in range(THRESHOLD - 1)]

def poly(x):
    return sum(c * pow(x, i, FIELD) for i, c in enumerate(coeffs)) % FIELD

points = [(i, poly(i)) for i in range(1, SHARES + 1)]
subset = points[:THRESHOLD]

recovered = lagrange_interpolate_zero(subset, FIELD)

print("Original secret:", SECRET)
print("Recovered secret:", recovered)
