grades = [0,0,0]
avg = 0

for  i in range(0,3):
    grades[i] = float(input("Ingrese la calificacion "+str(i+1)+"--->"))

for  i in range(0,2):
    avg += grades[i]

avg = avg /3

avg = (avg * 55) /10

final_exam = float(input("Ingrese la calificacion del examen final----->"))

final_work = float(input("Ingrese la calificacion del trabajo final----->"))
total = avg + final_exam + final_work


print("Parciales:"+str(avg))
print("Examen final:"+str(final_exam))
print("Trabajo final:"+str(final_work))
print("Total:"+str(total))








