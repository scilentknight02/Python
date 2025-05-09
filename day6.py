a = {12, 13, 14, 15, 16}
b = {14, 15, 16, 17, 18}
print(a|b) #return Union
print(a&b) #return intersection
print(a - b)
print(b - a)
print (a in  b)
print(a.issubset(b))

a = {12, 13, 14, 15, 16}
b = {14, 15, 16}
print(a.issubset(b))
print(b.issubset(a))