import math;

radio = float(input("Ingrese el radio"))

volume = (3/4) *math.pi * math.pow(radio,3)
area =  4 * math.pi * math.pow(radio,2)


print("EL volumen es "+str(volume))
print("EL area es "+str(area))
