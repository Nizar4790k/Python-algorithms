import math

values = [0,0,0]

geometric_mean = 1

for  i in range(0,3):
    values[i] = float(input("Ingrese el valor "+str(i+1)+"--->"))

print(values)

for  i in range(0,3):
    geometric_mean *= values[i]

geometric_mean = math.pow(geometric_mean,1/3)

print("geomeric_mean---->"+str(geometric_mean))


