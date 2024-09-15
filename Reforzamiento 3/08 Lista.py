from numpy.ma.extras import median

var1=[0]*10
var1.append(int(input("Int: ")))
var1.append(int(input("Int: ")))
var1.append(int(input("Int: ")))
var1.append(int(input("Int: ")))
var1.append(int(input("Int: ")))
var1.append(int(input("Int: ")))
var1.append(int(input("Int: ")))
var1.append(int(input("Int: ")))
var1.append(int(input("Int: ")))
var1.append(int(input("Int: ")))

suma= sum(var1)
media= median(var1)
print(suma,media)