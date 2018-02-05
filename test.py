

import random
import numpy as np

ciao = [[0, 12], [1, 11], [1, 13]]

print(ciao)

i = 0

for x, y in ciao:

    x = x + 3
    ciao[i] = [x, y]
    i = i + 1

print(ciao)

random1 = random.randint(1, 6)
print(random1)
