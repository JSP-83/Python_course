# Modules et packages

# chargement
import math
print(math.sqrt(16))

# description module
help("math")
help("math.sqrt")

# import léger
from math import sqrt
print(sqrt(16))

# création espace de noms biblio_math via le module math
import math as biblio_math
biblio_math.sqrt(25)

# packages
from Biblio.multipli import table
print(table(5))

