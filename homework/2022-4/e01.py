# Nämä ovat muuttujat a ja b
a = "hello"
b = "world"

#print("hello world")
print("hello world") #Tämä printtaa hei maailma

# Nämä printtavat 
# muuttujia a ja b
# eri tavoin
print(a)
print(a,b)
print(a, b, sep=":")
print(a, b, sep=":", end =";")
print("\n")

"""
Tämä printtaa paljon välilyöntejä
"""
print(a, "\n", "\n")
print(b)

print(a, b, sep = "")

print(a, end = "")
print(b)

help(print)