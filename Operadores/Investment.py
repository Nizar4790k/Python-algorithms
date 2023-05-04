investor1 = float(input("Ingrese la cantidad del inversor 1"))
investor2 = float(input("Ingrese la cantidad del inversor 2"))
investor3 = float(input("Ingrese la cantidad del inversor 3"))

total_investment  = investor1+investor2+investor3

investor1_percentage =  investor1*100/total_investment
investor2_percentage =  investor2*100/total_investment
investor3_percentage =  investor3*100/total_investment

print("El porcentaje del inversor1 es: "+str(investor1_percentage))
print("El porcentaje del inversor2 es: "+str(investor2_percentage))
print("El porcentaje del inversor3 es: "+str(investor3_percentage))
