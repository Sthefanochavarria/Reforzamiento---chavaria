var1={}
for a in range(4):
    var2 = float(input("Ingrese un numero {}: ".format(a + 1)))

cubo= var2 ** 3

var1["var2"]=cubo
print(var1)