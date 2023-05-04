hours = float(input("Ingrese las horas"))
minutes = float(input("Ingrese los minutos"))
seconds = float(input("Ingrese los segundos"))

seconds = (hours* 3600) + (minutes* 60) + seconds

print("The seconds are "+str(seconds))
