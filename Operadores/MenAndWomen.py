
men_quantity = float(input("Ingrese la cantidad de hombres"))
women_quantity = float(input("Ingrese la cantidad de mujeres"))

total_students  = men_quantity+women_quantity

men_percentage= men_quantity*100/total_students
women_percentage = women_quantity *100/total_students

print("El porcentaje de hombres es: "+str(men_percentage))
print("El porcentaje de hombres es: "+str(women_percentage))


