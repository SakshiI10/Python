# Concept 2: DIctionary don't have a concecpt of indexing, the values are changed using keys.

c = {}
c[1] = 1
c['1'] = 2
c[1] += 1
print(c)